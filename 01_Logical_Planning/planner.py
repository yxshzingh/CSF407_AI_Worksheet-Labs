from collections import deque
from dataclasses import dataclass

@dataclass(frozen=True)
class Action:
    name: str
    positive_pre: frozenset
    negative_pre: frozenset
    positive_eff: frozenset
    negative_eff: frozenset

    def applicable(self, state):
        return self.positive_pre <= state and self.negative_pre.isdisjoint(state)

    def apply(self, state):
        return (state - self.negative_eff) | self.positive_eff


def bfs_plan(initial, goal, actions):
    initial = frozenset(initial)
    goal = frozenset(goal)
    q = deque([(initial, [])])
    visited = {initial}
    while q:
        state, plan = q.popleft()
        if goal <= state:
            return plan, state
        for action in actions:
            if action.applicable(state):
                nxt = action.apply(state)
                if nxt not in visited:
                    visited.add(nxt)
                    q.append((nxt, plan + [action]))
    return None, None


def run_tests():
    move_ab = Action('Move(A,B)', frozenset({'At(Robot,A)'}), frozenset(), frozenset({'At(Robot,B)'}), frozenset({'At(Robot,A)'}))
    move_ba = Action('Move(B,A)', frozenset({'At(Robot,B)'}), frozenset(), frozenset({'At(Robot,A)'}), frozenset({'At(Robot,B)'}))
    move_bc = Action('Move(B,C)', frozenset({'At(Robot,B)'}), frozenset(), frozenset({'At(Robot,C)'}), frozenset({'At(Robot,B)'}))
    move_cb = Action('Move(C,B)', frozenset({'At(Robot,C)'}), frozenset(), frozenset({'At(Robot,B)'}), frozenset({'At(Robot,C)'}))
    pickup_a = Action('PickUp(Package,A)', frozenset({'At(Robot,A)','At(Package,A)'}), frozenset(), frozenset({'Holding(Package)'}), frozenset({'At(Package,A)'}))
    pickup_b = Action('PickUp(Package,B)', frozenset({'At(Robot,B)','At(Package,B)'}), frozenset(), frozenset({'Holding(Package)'}), frozenset({'At(Package,B)'}))
    drop_c = Action('Drop(Package,C)', frozenset({'At(Robot,C)','Holding(Package)'}), frozenset(), frozenset({'At(Package,C)'}), frozenset({'Holding(Package)'}))
    actions = [move_ab, move_ba, move_bc, move_cb, pickup_a, pickup_b, drop_c]
    initial = {'At(Robot,A)','At(Package,A)'}
    goal = {'At(Package,C)'}
    plan, final = bfs_plan(initial, goal, actions)
    assert plan is not None
    state = frozenset(initial)
    states = [state]
    for a in plan:
        assert a.applicable(state), a.name
        state = a.apply(state)
        states.append(state)
    assert goal <= state

    impossible_actions = [a for a in actions if not a.name.startswith('PickUp')]
    no_plan, _ = bfs_plan(initial, goal, impossible_actions)
    assert no_plan is None

    irrelevant = Action('Move(A,B)', frozenset({'At(Robot,A)'}), frozenset(), frozenset({'At(Robot,B)'}), frozenset({'At(Robot,A)'}))
    plan2, final2 = bfs_plan(initial, goal, [irrelevant])
    assert plan2 is None

    print('TEST A: Solvable')
    print('Plan:', ' -> '.join(a.name for a in plan))
    for i, s in enumerate(states): print(f'S{i}:', sorted(s))
    print('TEST B: Impossible:', 'No plan found' if no_plan is None else 'Unexpected plan')
    print('TEST C: Irrelevant actions:', 'No plan found' if plan2 is None else 'Unexpected plan')

if __name__ == '__main__':
    run_tests()
