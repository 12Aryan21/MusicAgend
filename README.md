                     README.md
# MoodMusic Trash Agent (V0.1)

A humorous, rule-based command-line program that detects a user’s emotional mood from text input and recommends a music track. The project intentionally incorporates chaotic elements, sarcastic prompts, and randomized selection to create an entertaining interaction experience.

---

## Features
- Lightweight natural-language preprocessing.
- Keyword and synonym-based mood detection.
- Random tie-breaking to simulate variability.
- Mood-aligned track recommendations (multiple choices per mood).
- Command-line interface with humorous and intentionally "trash-tier" dialogue.

---

## How It Works
1. User enters a short phrase describing their feelings.
2. The agent tokenizes and preprocesses the text.
3. Words are matched against:
   - A mood-specific catalog
   - A synonym mapping dictionary
4. The strongest-matched mood is selected.
5. A random track associated with that mood is returned.
6. If no mood is detected, a sarcastic fallback message is displayed.

---

## Requirements
- Python 3.x
- Standard library only (no external dependencies)

---

## How to Run
```bash
python3 moodmusic_trash_agent.py
When prompted, type your mood or emotional statement.
To exit, type:
quit
________________________________________
Example Interaction
[MoodMusic Trash Agent V0.1 Initialized]
Fine, tell me your feelings. I'm listening (reluctantly).
Your Mood/Query (HURRY UP): feeling kind of anxious today

--- INCREDIBLY IMPORTANT ANALYSIS & RECOMMENDATION ---
My very simple algorithm suggests, obviously, 'ANXIOUS' (TRASH SCORE: 1).
YOUR RECOMMENDATION: GENRE IS: Ambient --- TRACK IS: DEEP FOCUS WAVE - ZENSOUNDS
________________________________________
Folder Structure
/moodmusic_trash_agent
 ├── moodmusic_trash_agent.py
 ├── README.md
 ├── statement.md
 └── docs/
      └── project_report.md
________________________________________
Notes
•	This project is intentionally humorous but functionally complete.
•	Mood detection is rule-based and relies entirely on keyword matching.
•	Music recommendations are randomized within each mood category.

---

# ✅ **docs/project_report.md**

```md
# Project Report: MoodMusic Trash Agent (V0.1)

## 1. Introduction
This project implements a command-line “mood detection” agent that converts user-entered emotional text into a music recommendation. The design intentionally blends functional rule-based NLP with humorous and unpredictable system behavior. The purpose is to demonstrate text processing, classification logic, and randomized recommendation techniques using pure Python.

---

## 2. Problem Statement
The challenge is to map free-text emotional expressions to a set of predefined mood categories. Users might express emotions in varied ways, including slang, synonyms, or ambiguous statements. This project provides a simplified pipeline for mood extraction and uses mood-to-music mapping to return a recommended track.

---

## 3. Functional Requirements
- Accept user input continuously through CLI.
- Tokenize and normalize the input text.
- Detect mood keywords from the catalog.
- Check for synonyms when no direct match exists.
- Generate a mood classification using frequency counts.
- Break ties using random choice.
- Recommend one music track from the corresponding mood category.
- Provide fallback responses when no mood is detected.

---

## 4. Non-Functional Requirements
- **Performance:** Must operate instantly on small text inputs.
- **Usability:** Simple CLI with short instructions.
- **Maintainability:** Modular functions for preprocessing, detection, and recommendation.
- **Reliability:** Basic exception handling to prevent crashes.
- **Portability:** Uses only Python standard libraries.
- **User Engagement:** Humorous and informal responses.

---

## 5. System Architecture
**Main Components:**
- **Preprocessing Module**  
  - Lowercases text, removes punctuation, and tokenizes.
- **Mood Detection Engine**  
  - Counts keyword occurrences and synonym matches.
  - Resolves ties using randomness.
- **Recommendation Engine**  
  - Chooses one random track associated with detected mood.
- **CLI Handler**  
  - Handles user input, prints output, and manages loop control.

---

## 6. Workflow Diagram (High-Level)

User Input
↓
Text Preprocessing
↓
Keyword + Synonym Matching
↓
Mood Classification
↓
Track Recommendation
↓
Output to CLI (Humorous Response)

---

## 7. Design Decisions & Rationale
- **Rule-based classification** was chosen over ML to keep the project deterministic and transparent.
- **Random tie-breaking** adds variety and simulates non-determinism.
- **Multiple tracks per mood** increases recommendation diversity.
- **Humorous tone** enhances engagement and differentiates the agent from conventional chatbots.
- **Standard-library-only** ensures portability and simplicity.

---

## 8. Implementation Details
### Key Functions
- `data_preprocess_and_tokenize_for_mood_detection_v1()`  
  Handles cleaning and splitting text.
- `identify_best_emotional_state()`  
  Performs counting, synonym resolution, and tie-breaking.
- `get_a_track_based_on_mood_id()`  
  Selects a track from the associated mood playlist.
- `run_the_music_vibe_thing_cli()`  
  Interactive CLI loop.

### Data Structures
- `BAD_MUSIC_CATALOG`: Dictionary mapping moods → list of tracks.  
- `BAD_SYNONYMS_STRUCT`: Synonym mapping.  
- Several humorous string lists for dynamic, sarcastic output.

---

## 9. Testing Approach
- Manual testing using various emotional expressions.
- Synonym testing (e.g., “depressed” → “sad”).
- Stress testing for empty input, unknown words, and long text.
- Verified random tie-breaking through repeated runs.

---

## 10. Sample Test Inputs & Outputs

**Input:**  
`I'm feeling very mellow today, just chilling.`  
**Output:**  
Detected `"mellow"` with track recommendation.

**Input:**  
`Bro I'm hyper AND sleepy what is wrong`  
**Output:**  
Detected `"tired"` or `"energetic"` depending on randomization.

**Input:**  
`.....`  
**Output:**  
Fallback snark message.

---

## 11. Challenges Faced
- Handling unpredictable and slang-heavy input.
- Ensuring token randomness does not break mood detection.
- Designing humorous responses without overshadowing functionality.

---

## 12. Learnings & Key Takeaways
- Even simple NLP needs careful preprocessing.
- Rule-based classification works well with constrained vocabulary.
- Randomness makes CLI interactions feel more dynamic.
- Humor improves user engagement dramatically.

---

## 13. Future Enhancements
- Integrate Spotify/Youtube API links.
- Add sentiment analysis using lightweight NLP.
- Extend mood categories and track catalog.
- Improve synonym mapping using word embeddings.
- Add configuration file for custom playlists.

---

## 14. References
- Python Standard Library Documentation  
- Basic NLP preprocessing practices  
- Informal mood classification guides 
        
<img width="1483" height="666" alt="Screenshot 2025-11-24 215407" src="https://github.com/user-attachments/assets/fe9dd95a-74ad-4021-9504-6d6792a9135c" />
<img width="1456" height="924" alt="Screenshot 2025-11-24 215352" src="https://github.com/user-attachments/assets/9db4ddc4-cb23-4037-afa8-eebd3539d860" />
<img width="1578" height="730" alt="Screenshot 2025-11-24 215339" src="https://github.com/user-attachments/assets/2322d822-c286-4ecb-aaae-2a2fb93adc4d" />
<img width="1277" height="916" alt="Screenshot 2025-11-24 215327" src="https://github.com/user-attachments/assets/5337a032-8e71-44ef-9104-7ea2553c0016" />
<img width="1057" height="736" alt="Screenshot 2025-11-24 215313" src="https://github.com/user-attachments/assets/1bc4fdbe-dee7-411e-bdc5-72c379584f03" />
<img width="999" height="693" alt="Screenshot 2025-11-24 215301" src="https://github.com/user-attachments/assets/650eb5f9-c97d-4382-b82c-567f806a62b0" />
<img width="931" height="908" alt="Screenshot 2025-11-24 215248" src="https://github.com/user-attachments/assets/d6d4dddb-0b75-40a0-9bd9-b392c7fb0019" />
<img width="1617" height="1021" alt="Screenshot 2025-11-24 215215" src="https://github.com/user-attachments/assets/1ae59d03-99df-4253-ad2d-665f7d91a864" />
<img width="1491" height="1039" alt="Screenshot 2025-11-24 215153" src="https://github.com/user-attachments/assets/592a4520-1acc-42fb-bad7-fae93c9abea3" />







         

    



