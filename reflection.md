# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

One bug I encountered was the "Go LOWER" and "Go HIGHER" message after a guess would be inconsistent with my actual guess. For example, inputting a value of 1 would prompt the message "Go LOWER" even though the correct value is obviously higher than 1. A second bug I encountered was the "Attempts Left" count when a user would enter a guess. The count starts from 8, and once a user has guessed 7 times, it prompts the correct answer at the bottom of the screen even though the user still has one guess remaining. A third bug I encountered is the "New Game" button. Once the correct answer is shown after a user runs out of guesses, the "New Game" button doesn't reset the guess counter and users are not able to enter a new value (the screen is effectively stuck). 

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion you accepted and why.
- Give one example of an AI suggestion you changed or rejected and why.

Throughout this project, I used Copilot to assist me with debugging. One example of an AI suggestion I accepted is for the "New Game" bug, where users were unable to start a new game at any point. Copilot recommended adding "st.session_state.status = 'playing'" to ensure the bug would be fixed, and I implemented this fix. One example of an AI suggestion I changed is for the "Attempts left" counter, where the correct answer will show when user has 1 guess remaining instead of 0. To fix this, Copilot recommended I move the st.info block (currently in line 128 of app.py) below the "if submit" block as well as to delete the "with st.expander" block. Even though the "st.expander" block was a bug that showed users the correct answer within the game, it wasn't a bug I was trying to fix, so I only implemented the change with the "st.info" block and rejected the changes to the "st.expander" block. 

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

To determine if a bug was really fixed, I would save the changes I made and refresh the Glitchy Guesser app to see if the changes fixed the targeted bug. To test if users would see the correct answer after 0 guesses remain, CoPilot generated a pytest that simulated the aspects of the Glitchy Guesser app (secret number, number of attempts, etc.). Once the number of attempts is at 0, the status of the game is set to "lost" and the secret answer is revealed. This test ensures that the number of attempts left is 0 before the correct answer appears. 

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

The secret number would change every new game due to the implementation of "st.session_state.secret = random.randint(1, 100)". This is implemented in the "if new_game" loop, ensuring that a different number is the secret number only when a new game is started. Streamlit reruns the entire Python script every time a user interacts with a certain application. For the Glitchy Guesser app, "st.rerun()" is utilized within the "if new_game" loop so the entire code is ran through when a user starts a new game. Session states ensures that certain data isn't lost everytime a user starts a new game, giving users a consistent game experience. 

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

This project taught me how to better utilize the "inline editing" and "agent mode" features within Copilot, as well as identifying bugs within code. The "Add Context" option within Copilot was crucial in AI assisting me with debugging as I was able to provide Copilot the files I was working on, as it removed the possibility of Copilot looking at the wrong files or giving incorrect feedback based on code that doesn't exist. I found the inline editing to be the most valuable feature within Copilot as it pinpointed where changes would be made within the code, and I could either accept or reject the changes.   
