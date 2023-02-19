# MathVis

## Inspiration
When I was a young kid in my 1st and 2nd grade I always found exams to be very boring and the questions asked on these exams were really irrelevant. When we are that young we don't care about how many objects some hypothetical character has, but what is important is that we are enjoying the process of learning. So to assist the teachers in making the learning process enjoyable, I would like to present a tool to make the questions themselves fun and more involving.

## What it does
It takes the input from the user, which is a question from first/second grade level math. It then converts this question into a comic like format so that kids of that age group can have a fun time while trying to solve those questions. It currently only supports one type of question.

## How we built it 
Since it supports only one kind of question, the question was designed in a way to get the right prompt. The question gets converted to the desired prompt through simple string addition. Then this prompt is fed into the Open AI image generator api to get the desired images to construct the comic. First four separate images are made to show the different situations in the question, then these four images are stitched together to make a single comic strip. 

## Challenges we ran into
1. Designing the prompt for the question.

## Accomplishments that we're proud of
I was able to get the prompt for image generation right. So most of the times the comic generated is correct for the question asked.

## What we learned
How to code software 3.0, that is making use of prompts to code creative solutions. I also learned about how image processing works at a higher level. 

## What's next for MathVis
Supporting other types of questions, even venture out of the domain of math support other subjects.
