FA8_KHAFAJI
================
Mostafa Khafaji
2024-04-12

## 1. An analogue signal received at a detector, measured in microvolts, is normally distributed with mean of 200 and variance of 256

A. What is the probability that the signal will exceed 224 µV?

``` r
ave <- 200
standev <- sqrt(256)
a <- pnorm(224, mean = ave, sd = standev, lower.tail = FALSE)

cat("The probability that the signal will exceed 224 µV is:", a)
```

    ## The probability that the signal will exceed 224 µV is: 0.0668072

B. What is the probability that it will be between 186 µV and 224 µV?

``` r
b <- pnorm(224, mean = ave, sd = standev) - pnorm(186, mean = ave, sd = standev)

cat("The probability that it will be between 186 µV and 224 µV is: ", b)
```

    ## The probability that it will be between 186 µV and 224 µV is:  0.7424058

C. What is the µV below which 25% of the signals will be?

``` r
c <- qnorm(0.25, mean = ave, sd = standev)
cat("The µV below which 25% of the signals will be: ", c)
```

    ## The µV below which 25% of the signals will be:  189.2082

D. What is the probability that the signal will be less than 240µV,
given that it is larger than 210 µV?

by the formula for conditional probability:

P(x\<240\|x\>210)

= P(x\<240 ∩ x\>210)/P(x\>210)

= p(x\<240) - P(x\<=210) / 1 - P(x\<=210)

we can code this as:

``` r
d <- (pnorm(240, mean = ave, sd = standev) - pnorm(210, mean = ave, sd = standev))/pnorm(210, mean = ave, sd = standev, lower.tail = FALSE)
cat("The probability that the signal will be less than 240µV, given that it is larger than 210 µV, is : ",d)
```

    ## The probability that the signal will be less than 240µV, given that it is larger than 210 µV, is :  0.9766541

E. Estimate the interquartile range.

The interquartile range is the difference between the third and 1st
quartile, i.e. 75% and 25%, respectively.

``` r
e <- qnorm(0.75, mean = ave, sd=standev)-qnorm(0.25, mean = ave, sd=standev)
cat("The interquartile range is: ", e,"µV")
```

    ## The interquartile range is:  21.58367 µV

F. What is the probability that the signal will be less than 220 µV,
given that it is larger than 210 µV?

Like question D:

P(x\<220\|x\>210)

= P(x\<220 ∩ x\>210)/P(x\>210)

= p(x\<220) - P(x\<=210) / 1 - P(x\<=210)

``` r
f <- (pnorm(220, mean = ave, sd = standev) - pnorm(210, mean = ave, sd = standev))/pnorm(210, mean = ave, sd = standev, lower.tail = FALSE)
cat("The probability that the signal will be less than 220µV, given that it is larger than 210 µV, is : ",f)
```

    ## The probability that the signal will be less than 220µV, given that it is larger than 210 µV, is :  0.6027988

G. If we know that a received signal is greater than 200 µV, what is the
probability that it is in fact greater than 220 µV?

Formula of conditional probability gives us:

P(x\>220 \| x\>200)

= P(x\>220 ∩ x\>200)/P(x\>200)

= 1-P(x\<=220) / 1-P(x\<=200)

``` r
g <- pnorm(220, mean = ave, sd = standev, lower.tail = FALSE)/pnorm(200, mean = ave, sd = standev, lower.tail = FALSE)

cat("the probability that it is in fact greater than 220 µV, if we know that a received signal is greater than 200 µV, is: ", g)
```

    ## the probability that it is in fact greater than 220 µV, if we know that a received signal is greater than 200 µV, is:  0.2112995

## 2. anufacturer of a particular type of computer system is interested in improv- ing its customer support services. As a first step, its marketing department has been charged with the responsibility of summarizing the extent of customer problems in terms of system failures. Over a period of six months, customers were surveyed and the amount of downtime (in minutes) due to system failures they had experienced during the previous month was collected. The average downtime was found to be 25 minutes and a variance of 144. If it can be assumed that downtime is normally distributed:

    I. Obtain bounds which will include 95% of the downtime of the customers.


    ```r
    ave_dt <- 25
    sd_dt <- sqrt(144)
    i <- qnorm(0.95, mean = ave_dt, sd = sd_dt)
    cat("The upper bound which will include 95% of the downtime of the customers, in minutes, is: ",i)

    ## The upper bound which will include 95% of the downtime of the customers, in minutes, is:  44.73824

2.  Obtain the bound above which 10% of the downtime is included.

{r ca, echo=TRUEumii \<- qnorm(0.1, mean = ave_dt, sd = sd_dt) cat(“The
upper bound which will include 10% of the downtime of the customers, in
minutes, is:”,ii\`\`

## 
