FA3_KHAFAJI
================
Mostafa Khafaji
2024-02-25

## Question 1

A binary communication channel carries data as one of two sets of
signals denoted by 0 and 1. Owing to noise, a transmitted 0 is sometimes
received as a 1, and a transmitted 1 is sometimes received as a 0. For a
given channel, it can be assumed that a transmitted 0 is correctly
received with probability 0.95, and a transmitted 1 is correctly
received with probability 0.75. Also, 70% of all messages are
transmitted as a 0. If a signal is sent, determine the probability that:

1)  a 1 was received;
2)  a 1 was transmitted given than a 1 was received.

**a**

``` r
#probability/percentage that signals are transmitted
sig0_trans <- 0.7
sig1_trans <- 0.3

#probability of error in transmission
sig0_e <- sig0_trans*0.05
sig1_e <- sig1_trans*0.25
```

Since we can view signal transmission as mutually exclusive, and the
errors in transmission are within the probability of each transmission,
we can look at the problem as the union of success in signal 1, and the
error of signal 0, as such:

**sig1_success + sig0_error = sig1_total**

calculating the resultant probability:

``` r
sig1_total <- (sig1_trans-sig1_e)+sig0_e

cat("The percentage of the receiver getting a signal of 1 is: ",sig1_total*100,"%",sep = "")
```

    ## The percentage of the receiver getting a signal of 1 is: 26%

**(b)**

For b, we need to imagine a new venn diagram, in which sig1_total is a
proper superset of sig1_success, so then:

**sig1_total (intersection) sig1_success = sig1_success**

then, when looking for what is asked:

**p(sig1_success \| sig1_result) = p(sig1_total (intersection)
sig1_success)/p(sig1_total)**

**= p(sig1_success)/p(sig1_total)**

then, let us solve:

``` r
solveb <- (sig1_trans*0.75)/(sig1_total)
cat("the probability of a 1 was transmitted given than a 1 was received is ",solveb*100,"%",sep = "")
```

    ## the probability of a 1 was transmitted given than a 1 was received is 86.53846%

## Question 2

There are three employees working at an IT company: Jane, Amy, and Ava,
doing 10%, 30%, and 60% of the programming, respectively. 8% of Jane’s
work, 5% of Amy’s work, and just 1% of Ava‘s work is in error.

1)  What is the overall percentage of error?
2)  If a program is found with an error, who is the most likely person
    to have written it?

let us first set down the variables:

``` r
jane <- 0.1
jane_e <- jane*0.08
Amy <- 0.3
Amy_e <- Amy*0.05
Ava <- 0.6
Ava_e <- Ava*0.01
```

**(a)** As the work of each is mutually exclusive, and so are their
errors, we can simply add up the probability of their errors

``` r
tot_error <- jane_e + Amy_e + Ava_e
cat("The total probability of error is ",tot_error*100,"%",sep = "")
```

    ## The total probability of error is 2.9%

**(b)**

Here, we can use the same idea as Question 1 B., so that

**p(programmer_error \| error) = p(programmer_error)/p(error)**

we can then calculate for each.

``` r
#jane error
jane_fault <- jane_e / tot_error
cat("The probability of, when there is an error, it is Jane's program, is ",jane_fault*100,"%\n",sep = "")
```

    ## The probability of, when there is an error, it is Jane's program, is 27.58621%

``` r
#amy error
amy_fault <- Amy_e / tot_error
cat("The probability of, when there is an error, it is Amy's program, is ",amy_fault*100,"%\n",sep = "")
```

    ## The probability of, when there is an error, it is Amy's program, is 51.72414%

``` r
#ava fault
ava_fault <- Ava_e / tot_error
cat("The probability of, when there is an error, it is Ava's program, is ",ava_fault*100,"%\n",sep = "")
```

    ## The probability of, when there is an error, it is Ava's program, is 20.68966%

As seen from the results, the event that, when there is an error, it is
Amy’s program, is the highest.
