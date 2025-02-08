<test-cases>
    <case id="simple-1">
        <english>I want water.</english>
        <vocabulary>
            <word>
                <arabic>نحب</arabic>
                <latin>nheb</latin>
                <english>want</english>
                <origin>Arabic</origin>
            </word>
            <word>
                <arabic>ماء</arabic>
                <latin>ma</latin>
                <english>water</english>
                <origin>Arabic</origin>
            </word>
        </vocabulary>
        <structure>[Subject] [Verb] [Object].</structure>
        <considerations>
            - Basic sentence with subject, verb, object
            - Present tense form
            - Subject can be included or omitted since verb conjugation indicates it
        </considerations>
    </case>
    <case id="simple-2">
        <english>The house is big.</english>
        <vocabulary>
            <word>
                <arabic>دار</arabic>
                <latin>dar</latin>
                <english>house</english>
                <origin>Arabic</origin>
            </word>
            <word>
                <arabic>كبير</arabic>
                <latin>kbir</latin>
                <english>big</english>
                <origin>Arabic</origin>
            </word>
        </vocabulary>
        <structure>[Article] [Subject] [Adjective].</structure>
        <considerations>
            - Simple descriptor sentence
            - Uses adjective after noun
            - No verb needed in present tense
        </considerations>
    </case>
</test-cases>

### 1.2 Compound Sentences
```xml
<test-cases>
    <case id="compound-1">
        <english>I'm going to the market and buying bread.</english>
        <vocabulary>
            <word>
                <arabic>روح</arabic>
                <latin>ruh</latin>
                <english>go</english>
                <origin>Arabic</origin>
            </word>
            <word>
                <latin>marchi</latin>
                <english>market</english>
                <origin>French</origin>
            </word>
            <word>
                <arabic>خبز</arabic>
                <latin>khobz</latin>
                <english>bread</english>
                <origin>Arabic</origin>
            </word>
        </vocabulary>
        <structure>[Subject] [Present-Continuous] [Location] [Conjunction] [Verb] [Object].</structure>
        <considerations>
            - Compound sentence with two actions
            - Uses "rani rayeh" construction for present continuous
            - Conjunction "w" for "and"
        </considerations>
    </case>
</test-cases>

### 1.3 Complex Sentences
```xml
<test-cases>
    <case id="complex-1">
        <english>When I went home, I found my brother sleeping.</english>
        <vocabulary>
            <word>
                <arabic>روح</arabic>
                <latin>ruh</latin>
                <english>go</english>
                <origin>Arabic</origin>
            </word>
            <word>
                <arabic>دار</arabic>
                <latin>dar</latin>
                <english>house</english>
                <origin>Arabic</origin>
            </word>
            <word>
                <arabic>لقى</arabic>
                <latin>lqa</latin>
                <english>find</english>
                <origin>Arabic</origin>
            </word>
            <word>
                <arabic>خوي</arabic>
                <latin>khuya</latin>
                <english>brother</english>
                <origin>Arabic</origin>
            </word>
        </vocabulary>
        <structure>[Time-Marker] [Verb-Past], [Subject] [Verb-Past] [Object] [State].</structure>
        <considerations>
            - Uses "ki" for "when"
            - Past tense verbs
            - State description using active participle
        </considerations>
    </case>
</test-cases>

## 2. Vocabulary Edge Cases

### 2.1 French-Arabic Alternatives
```xml
<vocabulary-test>
    <word-pair>
        <french-origin>
            <latin>tomobil</latin>
            <english>car</english>
            <origin>French: automobile</origin>
        </french-origin>
        <arabic-origin>
            <arabic>كرهبة</arabic>
            <latin>karhba</latin>
            <english>car</english>
            <origin>Arabic</origin>
        </arabic-origin>
        <usage-notes>
            - Both terms are commonly used
            - Regional preferences may apply
            - French term more common in urban areas
        </usage-notes>
    </word-pair>
</vocabulary-test>

### 2.2 Verb Forms
```xml
<vocabulary-test>
    <verb>
        <arabic>كتب</arabic>
        <latin>kteb</latin>
        <english>write</english>
        <conjugations>
            <present>nekteb, tekteb, yekteb</present>
            <past>ktebt, ktebt, kteb</past>
            <future>nekteb, tekteb, yekteb</future>
        </conjugations>
        <test-sentences>
            <sentence>I write a letter.</sentence>
            <sentence>I wrote yesterday.</sentence>
            <sentence>I will write tomorrow.</sentence>
        </test-sentences>
    </verb>
</vocabulary-test>

## 3. State Transition Tests

### 3.1 Valid Transitions
```xml
<transition-test>
    <scenario id="setup-to-attempt">
        <initial-state>Setup</initial-state>
        <input>Ana rayeh lel marchi.</input>
        <expected-state>Attempt</expected-state>
        <validation>
            - Input contains Darja text
            - Uses vocabulary from setup
            - Attempts sentence structure
        </validation>
    </scenario>
</transition-test>

## 4. Teaching Scenario Tests

### 4.1 Common Mistakes
```xml
<teaching-test>
    <scenario id="present-continuous">
        <student-attempt>Ana ruh lel marchi.</student-attempt>
        <error>Incorrect present continuous formation</error>
        <expected-guidance>
            - Acknowledge attempt
            - Explain "rani rayeh" construction
            - Encourage new attempt
        </expected-guidance>
    </scenario>
    <scenario id="negation">
        <student-attempt>Ana ma ruh.</student-attempt>
        <error>Incomplete negation structure</error>
        <expected-guidance>
            - Point out missing "sh" suffix
            - Review negation pattern
            - Encourage correction
        </expected-guidance>
    </scenario>
</teaching-test>

## 5. Cultural Context Tests
```xml
<cultural-test>
    <scenario id="greetings">
        <context>Morning greeting to elder</context>
        <vocabulary>
            <word>
                <arabic>صباح</arabic>
                <latin>sbah</latin>
                <english>morning</english>
                <origin>Arabic</origin>
            </word>
            <word>
                <arabic>خير</arabic>
                <latin>khir</latin>
                <english>good</english>
                <origin>Arabic</origin>
            </word>
        </vocabulary>
        <considerations>
            - Respect markers in speech
            - Appropriate response expectations
            - Regional variations
        </considerations>
    </scenario>
</cultural-test>

## 6. Validation Criteria

### 6.1 Response Scoring
```xml
<scoring-criteria>
    <category name="vocabulary-table">
        <criteria>
            - Shows Arabic script only for Arabic-origin words (2 points)
            - Includes origin language (2 points)
            - Proper Latin transcription (2 points)
            - Appropriate difficulty level (2 points)
            - Common usage terms (2 points)
        </criteria>
    </category>
    <category name="sentence-structure">
        <criteria>
            - Clear pattern indication (2 points)
            - Appropriate for level (2 points)
            - Considers dialectal variations (2 points)
            - Matches natural speech (2 points)
            - Cultural appropriateness (2 points)
        </criteria>
    </category>
</scoring-criteria>