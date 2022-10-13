
#ifndef __ROLL_CONDITION_CHECKING_H__
#define __ROLL_CONDITION_CHECKING_H__


typedef enum {
    INVALID=0,
    EQUALS=1,
    GREATER_THAN=2,
    LESS_THAN=3,
    GREATER_OR_EQUALS=4,
    LESS_OR_EQUALS=5,
    NOT_EQUAL=6,
    UNIQUE=7
} COMPARATOR;

int check_condition(
    vec * x, 
    vec * y, 
    COMPARATOR c
);

int check_condition_scalar(
    int x, 
    int y, 
    COMPARATOR c
);
#endif
