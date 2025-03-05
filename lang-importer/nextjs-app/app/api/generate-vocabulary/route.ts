import { type NextRequest, NextResponse } from "next/server"
import { createOpenAI as createGroq } from "@ai-sdk/openai"
import { generateObject } from "ai"
import { z } from "zod"

// Define the vocabulary item schema
const vocabularyItemSchema = z.object({
  latin_spelling: z.string().describe("The word in Latin script"),
  origin_language: z.string().nullable().describe("The original language the word derived from. Null if unknown"),
  arabic_spelling: z.string().nullable().describe("The word in Arabic script written from right to left when the origin language is Arabic"),
  english: z.string().describe("The English translation"),
})

// Define the response schema
const responseSchema = z.object({
  data: z.array(vocabularyItemSchema)
});

export async function POST(request: NextRequest) {
  try {
    const { thematicCategory } = await request.json()

    if (!thematicCategory) {
      return NextResponse.json({ error: "Thematic category is required" }, { status: 400 })
    }

    // Check if GROQ_API_KEY is available
    const apiKey = process.env.GROQ_API_KEY
    if (!apiKey) {
      return NextResponse.json({ error: "GROQ API key is not configured" }, { status: 500 })
    }

    // Initialize Groq client
    const groq = createGroq({
      apiKey,
      baseURL: "https://api.groq.com/openai/v1",
    })

    // Generate vocabulary using Groq LLM
    const response = await generateObject({
      model: groq("qwen-2.5-32b"),
      schema: responseSchema,
      prompt: `Generate 5 vocabulary items in Algerian darja related to the thematic category "${thematicCategory}". 
Each item should include the word in Latin script, the language of origin, the word in Arabic script for words where the origin language is Arabic, and the English translation.
Respond STRICTLY in the following JSON format, with no additional text:
  {
  "data": [
    {
      "latin_spelling": "...",
      "origin_language": "...",
      "arabic_spelling": null,
      "english": "..."
    },
    ...
  ]
}`,
      maxTokens: 250,
    })

    return NextResponse.json(response.object.data)
  } catch (error) {
    console.error("Error generating vocabulary:", error)
    return NextResponse.json({ error: "Failed to generate vocabulary" }, { status: 500 })
  }
}

