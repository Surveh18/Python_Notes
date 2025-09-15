# U can vote or not
# With parameter with return.


def vote(age: int) -> str:
    if age < 18:
        return "You cannot vote"
    return "You can vote"  # feasible output.(the thing which we want first.)


ans = vote(23)
print(ans)
# above is the best practice to solve 80% of time.


def election(age: int) -> None:
    if age < 18:
        print("You are not eligible")
        return
    print("You are eligible")


(election(17))
