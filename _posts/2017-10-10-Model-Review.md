---
layout: post
title: Model Review (Portfolio)
---
Any strategy is dependent on parameters. Constant parameters are preferred. However, the parameters are usually changing. We define the process to tune the parameters as "Model Review". 

Although this process is to tune parameters, it needs new parameters itself:
1. the lookback period to calculate what is the best parameter, NMonthLookBack
2. the period to conduct model review, NMonthModelReview

Example: for Time Series Momentum, we have parameters NDayTrain, NDayTest, NDayShift, NWeekStart to review. The best set of parameters is determined on its performance in the past NMonthLookBack, and the model review process will be conducted NMonthModelReview later. 

# What is the best (NMonthLookBack, NMonthModelReview)
For each (NMonthLookBack, NMonthModelReview), we have 10 value series with different review start date. Among them, the one with mininmum CR (worst) is selected as the score of this (NMonthLookBack, NMonthModelReview), which means we care the worst performance of (NMonthLookBack, NMonthModelReview). Of course, the (NMonthLookBack, NMonthModelReview) with the best worst-case performance is used, and its worst-case value series is as the Model Review version performance of the strategy. 

# Known problems
## The path dependency
The path dependency is only partially solved by use 10 different review start dates. Actually, a more reasonable method to determine the review start dates is also necessary

## How to tune (NMonthLookBack, NMonthModelReview)
The process of tuning parameter is always relying on new parmeter, and this is infinite loop. To solve this, we review the NMonthModelReview and NMonthLookBack every year, and this is fixed. 

