"use client"

import type React from "react"

import { useState } from "react"
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { Textarea } from "@/components/ui/textarea"
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import { ClipboardCopy, Loader2 } from "lucide-react"
import { toast } from "@/components/ui/use-toast"
import { Toaster } from "@/components/ui/toaster"

export default function VocabularyImporter() {
  const [thematicCategory, setThematicCategory] = useState("")
  const [result, setResult] = useState("")
  const [isLoading, setIsLoading] = useState(false)

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()

    if (!thematicCategory.trim()) {
      toast({
        title: "Error",
        description: "Please enter a thematic category",
        variant: "destructive",
      })
      return
    }

    setIsLoading(true)
    setResult("")

    try {
      const response = await fetch("/api/generate-vocabulary", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ thematicCategory }),
      })

      if (!response.ok) {
        const errorData = await response.json()
        throw new Error(errorData.error || "Failed to generate vocabulary")
      }

      const data = await response.json()
      setResult(JSON.stringify(data, null, 2))
    } catch (error) {
      console.error("Error generating vocabulary:", error)
      toast({
        title: "Error",
        description: error instanceof Error ? error.message : "Failed to generate vocabulary",
        variant: "destructive",
      })
    } finally {
      setIsLoading(false)
    }
  }

  const copyToClipboard = () => {
    navigator.clipboard.writeText(result)
    toast({
      title: "Success",
      description: "Copied to clipboard!",
    })
  }

  return (
    <Card>
      <CardHeader>
        <CardTitle>Generate Vocabulary</CardTitle>
        <CardDescription>Enter a thematic category to generate language vocabulary</CardDescription>
      </CardHeader>
      <CardContent>
        <form onSubmit={handleSubmit} className="space-y-4">
          <div className="space-y-2">
            <label htmlFor="category" className="text-sm font-medium">
              Thematic Category
            </label>
            <Input
              id="category"
              placeholder="e.g., Food, Colors, Family members"
              value={thematicCategory}
              onChange={(e) => setThematicCategory(e.target.value)}
              disabled={isLoading}
            />
          </div>
          <Button type="submit" className="w-full" disabled={isLoading}>
            {isLoading ? (
              <>
                <Loader2 className="mr-2 h-4 w-4 animate-spin" />
                Generating...
              </>
            ) : (
              "Generate Vocabulary"
            )}
          </Button>
        </form>

        {result && (
          <div className="mt-6 space-y-2">
            <div className="flex justify-between items-center">
              <h3 className="text-lg font-medium">Result</h3>
              <Button variant="outline" size="sm" onClick={copyToClipboard}>
                <ClipboardCopy className="h-4 w-4 mr-2" />
                Copy
              </Button>
            </div>
            <Textarea readOnly value={result} className="font-mono h-64 overflow-auto" />
          </div>
        )}
      </CardContent>
      <Toaster />
    </Card>
  )
}

