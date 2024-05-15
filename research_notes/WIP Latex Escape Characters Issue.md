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

## Background: Raw Strings

## Solution 1: Advise users to leverage raw strings in python but not to use \n

## Solution 2: Move straight to JSON only and get rid of all python versioning which may solve it

## Solution 3: Add a parser that when turned on parses all strings in MSML to be raw strings

## Solution 4: Add a parser that goes through and only changes some of the escape characters to have double slashes, i.e. ignore new line characters

## Solution 5: Advise users to just add another slash before any escape characters


Is there a way to do raw string that just filters some?