def vacuum_cleaner(state, pos):
    print(f"Initial: Pos {pos}, State {state}")
    for i in range(2):
        if state[pos] == 'Dirty':
            state[pos] = 'Clean'
            print(f"Cleaned room {pos}: {state}")
        pos = 1 - pos
        print(f"Moved to room {pos}")
    print(f"Final State: {state}")

state = ['Dirty','Dirty']
vacuum_cleaner(state, 0)
