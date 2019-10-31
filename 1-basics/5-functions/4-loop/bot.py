def crossed_bridge(steps):
    # Display each step
    step = 0
    while (step < steps):
        print("Crossed step.")
        step += 1

    # Display message
    if (steps > 5):
        print("The bridge is collapsing!")
    else:
        print("We must keep going!")