# WIP Latex Escape Characters Issue

## Problem Statement

When pasting over latex equations into a spec, there is an issue with escape characters. For example "\f" can end up not getting printed as \f but instead disappearing. There needs to be a way to handle this kind of issue within the MSML to make it as user friendly as possible.

The error is coming from the way python handles strings and parses escape characters automatically.

## Examples of the Problem

### An unwanted escape character

The following would create an issue because the code here:

    example1 = "$\frac{1}{2}$"
    print(example1)

Returns this:

    $rac{1}{2}$

### An unwanted escape character but also a wanted escape character (new line)

The following would create an issue because the code here:

    example2 = """$\frac{1}{2}$\n$\frac{1}{2}$"""
    print(example2)

Returns this:

    $rac{1}{2}$
    $rac{1}{2}$

## Background: Raw Strings in Python

- By putting r before a string, python can create a raw string which does not use any of the escape characters.
- One can also do double backslashes to turn off the escape character

## Solution 1: Advise users to leverage raw strings in python but not to use \n

- In this solution, FAQ would be updated with a note that one should use raw strings when defining strings for certain areas of MSML such as logic that might leverage latex/escape characters
- It would be required to also note that \n would no longer work and a user would have to use block strings for any new lines

## Solution 2: Move straight to JSON only and get rid of all python versioning which may solve it
- JSON might be a better fit with escape characters but there still is some risk that parsing is not perfect
- Also it might be premature to move to this step

## Solution 3: Add a parser that when turned on parses all strings in MSML to be raw strings
- This would be an automation on to solution 1, but would also still require warning about new line characters
- Also the feasibility of it is not definite, it may be the case that once a string is defined it can't be reverted to a raw string

## Solution 4: Add a parser that goes through and only changes some of the escape characters to have double slashes, i.e. ignore new line characters
- The parser could be turned on or off so that a user can have it automatically take strings like \f and replace them with \\\f

## Solution 5: Advise users to just add another slash before any escape characters
- It works but it also makes the user interface much worse because a user will need to constantly check these things

## Commentary

- I lean heavily on the recommendation of doing solution 4 as it seems like the best UI and also the most flexible.

