# WIP Latex Escape Characters Issue

## Problem Statement

## Examples of the Problem

### An unwanted escape character

    example1 = "$\frac{1}{2}$"
    print(example1)

### An unwanted escape character but wanted escape character (new line)

    example2 = """$\frac{1}{2}$\n$\frac{1}{2}$"""
    print(example2)

## Background: Raw Strings

## Solution 1: Advise users to leverage raw strings in python

## Solution 2: Move straight to JSON only and get rid of all python versioning which may solve it

## Solution 3: Add a parser that when turned on parses all strings in MSML to be raw strings

## Solution 4: Add a parser that goes through and only changes some of the escape characters to have double slashes, i.e. ignore new line characters


Is there a way to do raw string that just filters some?