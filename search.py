# coding=utf-8
# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    from game import Directions

    stack = util.Stack()  # برای اینکه  dfs بزنیم باید از استک استفاده کنیم
    our_state1 = problem.getStartState()  # ببینیم در کجا هستیم در اول کار

    list_see = [our_state1]
    if problem.isGoalState(our_state1):  # اگر جایی که هستیم همان گول هست سرجای خودمان بمانیم
        return [Directions.STOP]

    else:

        where_can_I_go = problem.getSuccessors(our_state1)  # بچه ها را به عنوان جاهایی که میتوانیم به استک اضافه کنیم

        for item in where_can_I_go:
            stack.push(
                ([item[1]], item[0]))  # برای اینکه با تابع تست کار کنه مجبور شدم به شکلی که سوال میخواست کد رو در بیارم
            # list_see.append(item[0])  #  نبود  autogrer  اگر تابع
        while not stack.isEmpty():  # تا زمانی که هدف پیدا نشده به گشتن ادامه میدیم

            our_state = stack.pop()
            if our_state[1] not in list_see:  # اگر جز جاهایی که ندیدیم نباشه
                list_see.append(our_state[1])  # به لیست جاهایی که دیدیم این نود را اضافه میکنیم
                if problem.isGoalState(
                        our_state[1]):  # در صورت پیروزی مسیری که منجر به این پیروزی شده است را برمیگردانیم
                    return our_state[0]
                where_can_I_go = problem.getSuccessors(our_state[1])

                for item in where_can_I_go:  # به expond نود هایی که پدر دیده در مسیر میپردازیم
                    # if list_see.count(item[0]) == 0:
                    stack.push((our_state[0] + [item[1]], item[0]))
                    # list_see.append(item[0])

    util.raiseNotDefined()


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    import time
    from game import Directions

    queue = util.Queue()
    our_state1 = problem.getStartState()  # برای اینکه  bfs بزنیم باید از صف استفاده کنیم
    list_see = [our_state1]

    if problem.isGoalState(our_state1):
        return [Directions.STOP]  # اگر جایی که هستیم همان گول هست سرجای خودمان بمانیم
    else:

        where_can_I_go = problem.getSuccessors(our_state1)

        for item in where_can_I_go:  # برای اینکه با تابع تست کار کنه مجبور شدم به شکلی که سوال میخواست کد رو در بیارم
            # list_see.append(item[0])  #  نبود  autogrer  اگر تابع
            queue.push(([item[1]], item[0]))

        while not queue.isEmpty():

            our_state = queue.pop()
            if our_state[1] not in list_see:
                list_see.append(our_state[1])
                if problem.isGoalState(
                        our_state[1]):  # در صورت پیروزی مسیری که منجر به این پیروزی شده است را برمیگردانیم
                    return our_state[0]
                where_can_I_go = problem.getSuccessors(our_state[1])

                for item in where_can_I_go:  # به expond نود هایی که پدر دیده در مسیر میپردازیم
                    # if item[0] not in list_see:
                    #     list_see.append(item[0])
                    queue.push((our_state[0] + [item[1]], item[0]))

        return our_state[0]


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    from game import Directions

    priorityQ = util.PriorityQueue()
    our_state1 = problem.getStartState()  # چون میخواهیم براساس هزینه سرچ انجام بدیم باید لیست نودهای دیده شده همواره sort باشد پس از صف اولویت دار استفاده میکنیم
    list_see = [our_state1]

    if problem.isGoalState(our_state1):  # اگر جایی که هستیم همان گول هست سرجای خودمان بمانیم
        return [Directions.STOP]

    else:

        where_can_I_go = problem.getSuccessors(our_state1)

        for item in where_can_I_go:
            priorityQ.push(([item[1]], item[0]), problem.getCostOfActions([item[1]]))

            # list_see.append(item[0])

        while not priorityQ.isEmpty():  # تا زمانی که هدف پیدا نشده به گشتن ادامه میدیم

            our_state = priorityQ.pop()
            if our_state[1] not in list_see:
                list_see.append(our_state[1])
                if problem.isGoalState(our_state[
                                           1]):  # در صورت پیروزی مسیری که منجر به این پیروزی شده است را برمیگردانیم که مسیر با کمترین هزینه باید باشد
                    return our_state[0]
                where_can_I_go = problem.getSuccessors(our_state[1])

                for item in where_can_I_go:
                    # if list_see.count(item[0]) == 0:
                    priorityQ.push((our_state[0] + [item[1]], item[0]),
                                   problem.getCostOfActions(our_state[0] + [item[1]]))
                    # list_see.append(item[0])
    util.raiseNotDefined()


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"

    from game import Directions

    priorityQ = util.PriorityQueue()  # برای اینکه *a را پیدا سازی کنیم به صف الویت دار نیاز داریم
    our_state1 = problem.getStartState()
    list_see = [our_state1]
    first_cost = heuristic(our_state1, problem)
    if problem.isGoalState(our_state1):
        return [Directions.STOP]

    else:

        where_can_I_go = problem.getSuccessors(our_state1)

        for item in where_can_I_go:

            priorityQ.push(([item[1]], item[0], first_cost + item[2]), first_cost + heuristic(item[0], problem) + item[2])
            # مقدر هزینه را به عنوان خروجی تابع heuristic براساس موقیعت اول و مکان فعلی محاسبه میکنه و براساس همین آیتم ها sort میشن

            # list_see.append(item[0])

        while not priorityQ.isEmpty():  # تا زمانی که به هدف نرسیده باشیم

            our_way, our_state, cost = priorityQ.pop()
            if our_state not in list_see:  # این مسیر را ندیده باشیم
                list_see.append(our_state)
                if problem.isGoalState(our_state):  # به هدف برسیم مسیر را برمگیردانیم
                    return our_way
                where_can_I_go = problem.getSuccessors(our_state)

                for item in where_can_I_go:
                    # if list_see.count(item[0]) == 0:
                    priorityQ.push((our_way + [item[1]], item[0], cost + item[2]),cost + item[2] + heuristic(item[0], problem))
                    #هزینه ای که باید برای رسیدن به این مرحله به پردازیم به علاوه هزینه جدید هیرستیکمان و اینکه هزینه قدیمی را باید ذخیره کنیم
                    # list_see.append(item[0])


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
