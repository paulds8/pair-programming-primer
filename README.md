# 🧑‍🤝‍🧑 Introduction to Pair Programming 🧑‍🤝‍🧑

Pair programming is a software development technique in which two programmers
work together at one "workstation". A common pattern is the driver-navigator
paradigm. One, the driver, writes code while the other, the navigator, reviews
each line of code as it is typed in, thinks ahead to the next steps, and
communicates with the driver. This allows for a division of labor and helps to
catch potential errors and improve the overall quality of the code. The two
programmers switch roles frequently.

## Benefits of Pair Programming

- Increased productivity
- Improved code quality
- Faster learning for new team members
- Reduced number of bugs
- Increased knowledge sharing

## Tips for success

- **Clearly communicate roles and goals**

  Before starting to pair program, both programmers should understand their
  roles and the goals of the task at hand. This can help ensure that everyone is
  on the same page and working towards the same objectives.

- **Take turns as driver and navigator**

  To ensure that both programmers are actively engaged in the process, it's
  important to switch roles frequently. This will help prevent one programmer
  from dominating the process and allow both programmers to learn from each
  other.

- **Use a consistent coding style**

  To make it easier to read and understand each other's code, it's important to
  use a consistent coding style. This can include things like indentation,
  naming conventions, and commenting practices.

- **Regularly commit and push changes**

  Pair programming can generate a lot of changes, so it's important to commit
  and push changes regularly. This will help ensure that both programmers have a
  copy of the latest code and can easily revert to previous versions if needed.

- **Take breaks and discuss issues**

  Pair programming can be intense, so it's
  important to take breaks and discuss any issues that arise. This can help
  prevent burnout and ensure that both programmers are on the same page
  regarding any challenges that arise.

## A Small Pair Programming Exercise

### Getting started [10 mins]

1. Split up into pairs. You will take turns being a "driver" and a "navigator".
   Decide who will be participant A and who will be participant B.
2. We will use VS Code for this exercise. Ensure both of you have the "Live Share"
   extension installed.
3. Participant A: clone this repo to you machine and start a live share session
   by clicking the Live Share icon in your side menu bar and clicking "Share".
   You may be asked to sign-in. Once the session is initiated, send the URL
   which should have automatically copied to your clipboard to your partner.
4. Participant B: follow the link and when prompted click "Open in VS Code".
   Follow the prompts.
5. Participant A: Keep an eye on the lower right of your screen for a pop-up;
   you need to accept the connection. Once this is done, you should now see your
   partner's name under "Participants". If your partner is in read-only mode,
   right click their name and enable read-write access.
6. Congratulations! You are both now in a live share session and ready to start
   pair programming in an interactive fashion.

### Task 1 [10 mins]

Participant A: Driver
Participant B: Navigator

1. Run `pip install -r requirements.txt` in your environment of choice (virtual
   environment recommended).
2. Take a look at `main.py`. Run the file and see what the output looks like.
3. When executed, this program queries an open exchange rate API with a given
   currency base; calculates the relative difference in percentage between the
   base currency and all the paired currencies; and finally prints the currency
   that it is strongest and weakest against.
4. Review `main.py` from the top down. Participant A will be driving (typing);
   Participant B will follow along and review each line of code in real time as
   you update this script, highlighting anything you've missed and making
   recommendations along the way. Both of you will have an active cursor for
   inputting code and highlighting exactly what you are referring to. Update the
   file to have a better coverage of things like exception handling, docstrings,
   comments, type hints, improved code readability, etc.

### Task 2 [10 mins]

Participant A: Navigator
Participant B: Driver

1. Switching roles (Participant B is in the driver's seat now), now take a look at
2. `test_main.py`. Currently there are only tests for `get_exchange_rates()`.
3. Run `pytest --cov-report term-missing --cov=main test_main.py` to see how
   much of the code is touched by this test. Participant A will need to give
   you permission to execute code in their terminal.
4. Check that the existing tests run either by clicking the Testing icon in the
   side menu and clicking the play button or executing `pytest` in the terminal.
   Note: currently it seems the Testing menu integration only works for the host
   of the live share session. The terminal method should definitely work for
   both the host and guests.
5. The purpose of this task is to write some tests for
   `convert_rate_to_percentage_difference()`. Use the existing tests as an
   example. Decide between the two of you what you would like to test. Write at
   least two tests. Participant B will now be typing with Participant A
   reviewing and providing help along the way.
6. Once your new tests run successfully, check how much you've improved the code
   coverage.

Congratulations! Your first pair programming session is complete. Getting
comfortable with pair programming can take some time at first, but it is worth
it in the long run as it allows for increased productivity, knowledge sharing,
and real-time problem solving. Getting practice in at being both the driver and
the navigator will ultimately make you a better programmer. There's also no
"right" way to do it either - the real benefit will come from making it a habit
as a team.
