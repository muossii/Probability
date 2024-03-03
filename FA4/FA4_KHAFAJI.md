FA4_KHAFAJI
================
Mostafa Khafaji
2024-03-03

## Question 1

A geospatial analysis System has four sensors supplying images. The
Percentage of Images Supplied by each sensor and the Percentage of
images relevant to a query are shown in the follwing table:

    ##   Sensor Percentage_of_Image_Supplied Percentage_of_Relevant_Image
    ## 1      1                         0.15                         0.50
    ## 2      2                         0.20                         0.60
    ## 3      3                         0.25                         0.80
    ## 4      4                         0.40                         0.85

**What is the overall percentage of Relevant Images?**

Then, to find out the percentage of each sensor’s relevant image to the
whole, we should **multiply the percentage of images supplied by each
sensor, to the percentage of relevant images of each sensor, then add
them together**

``` r
v_suppliedxrelevant <- apply(df1[, 2:3],c(1), prod)
overall_relevant_img <- sum(v_suppliedxrelevant)

cat("The overall percentage of relevant images is ", overall_relevant_img*100,"%",sep = "")
```

    ## The overall percentage of relevant images is 73.5%

## Question 2

A fair coin is tossed twice,

let E1 = (HH,TT) E2 = (HH,HT) E3 = (TH,HH)

Show that E1, E2, and E3 are pairwise independent but not mutually
independent.

We can start by creating a sample space square:

    ##    H1 T1
    ## H2 HH TH
    ## T2 HT TT

First, let’s check for pairwise independence, which states that

E1 and E2 are pairwise independent if:

p(E1 ∩ E2) = p(E1)p(E2)

Let’s start with E1 and E2, notice that their intersection is the toss
“HH”, which has a probability of 1/4.

Notice, also, that E1 and E2 both have a probability of 1/2 **P(E1) =
P(HH)+p(TT)=1/4 + 1/4 P(E2) = p(HH)+p(HT)=1/4+1/4**

p(E1)p(E2) = 1/2 \* 1/2 = 1/4,

p(E1)p(E2) = 1/4 = p(E1 ∩ E2)

**E1 and E2 are Pairwise independent.**

**We can do the same to E1 and E3:**

Show: p(E1 ∩ E3) = p(E1)p(E3)

p(E1 ∩ E3) = P(HH) = 1/4

**P(E1) = P(HH)+p(TT)=1/4 + 1/4 = 1/2 P(E3) = p(HH)+p(TH)=1/4+1/4 =
1/2**

p(E1)p(E3) = 1/2 \* 1/2 = 1/4

p(E1)p(E3) = 1/4 = p(E1 ∩ E3)

**E1 and E3 are Pairwise independent**

For E2 and E3:

Show: p(E2 ∩ E3) = p(E2)p(E3)

p(E2 ∩ E3) = P(HH) = 1/4

**P(E2) = p(HH)+p(HT)=1/4+1/4 = 1/2 P(E3) = p(HH)+p(TH)=1/4+1/4 = 1/2**

p(E2)p(E3) = 1/2 \* 1/2 = 1/4 = p(E2 ∩ E3)

p(E2)p(E3) = 1/4 = p(E2 ∩ E3)

**E2 and E3 are Pairwise independent**

**E1, E2, AND E3 ARE ALL PAIRWISE INDEPENDENT**

Now, let’s check for Mutual Independence

By definition, E1, E2, AND E3 are mutually independent if and only if:

p(E1 ∩ E2 ∩ E3) = P(E1) \* P(E2) \* P(E3)

We know that:

p(E1 ∩ E2 ∩ E3) = p(HH) = 1/4

and:

P(E1) = P(HH)+p(TT)=1/4 + 1/4 = 1/2 P(E2) = p(HH)+p(HT)=1/4+1/4 = 1/2  
P(E3) = p(HH)+p(TH)=1/4+1/4 = 1/2

P(E1) \* P(E2) \* P(E3) = 1/2 \* 1/2 \* 1/2 = 1/8

1/4 ≠ 1/8

**E1, E2 AND E3 ARE NOT MUTUALLY EXCLUSIVE**
