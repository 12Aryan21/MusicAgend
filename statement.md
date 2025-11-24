 Project Statement: MoodMusic Trash Agent (V0.1)

 Problem Statement
Users often express their emotional state or current mood through free-text messages. This project provides a rule-based command-line agent that interprets these mood cues and recommends an appropriate music track. The goal is to map informal, noisy user input to a simplified emotional category and return a suitable song recommendation.

 Scope of the Project
The system:
- Accepts natural-language mood descriptions from the user.
- Performs lightweight preprocessing and keyword detection.
- Maps mood expressions and synonyms to primary mood labels.
- Uses a catalog of tracks associated with each mood.
- Provides a track recommendation along with a confidence score.

 Target Users
- Students or users looking for quick, mood-based song suggestions.
- Individuals who prefer simple, command-line utilities.
- Users who want fun or humorous music recommendations in an interactive form.

 High-Level Features
- Tokenization and basic text preprocessing.
- Mood detection using direct keywords and synonym mapping.
- Tie-breaking and randomness to simulate variability.
- Music recommendation based on selected mood category.
- CLI interaction with humorous feedback for engagement.
