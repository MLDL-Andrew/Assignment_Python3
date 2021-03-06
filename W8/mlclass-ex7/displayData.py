import math
import matplotlib.pyplot as plt
import numpy as np

def displayData(X, example_width=None):
#DISPLAYDATA Display 2D data in a nice grid
#   [h, display_array] = DISPLAYDATA(X, example_width) displays 2D data
#   stored in X in a nice grid. It returns the figure handle h and the
#   displayed array if requested.

    # using plt.ion() instead of the commented section below
    # # closes previously opened figure. preventing a
    # # warning after opening too many figures
    # plt.close()

    # # creates new figure
    # plt.figure()

    # turns 1D X array into 2D
    if X.ndim == 1:
        X = np.reshape(X, (-1,X.shape[0]))

    # Set example_width automatically if not passed in
    if not example_width or not 'example_width' in locals():
        example_width = int(round(math.sqrt(X.shape[1])))

    print(example_width)
    # Gray Image
    plt.set_cmap("gray")

    # Compute rows, cols
    m, n = X.shape
    example_height = int(math.ceil(n / example_width))

    # Compute number of items to display
    display_rows = int(math.floor(math.sqrt(m)))
    print(display_rows)
    display_cols = int(math.ceil(m / display_rows))
    print(display_cols)
    # Between images padding
    pad = 1

    # Setup blank display
    print(example_height + pad)
    print(pad + display_rows * (example_height + pad))
    display_array = -np.ones((pad + display_rows * (example_height + pad),  pad + display_cols * (example_width + pad)))

    # Copy each example into a patch on the display array
    curr_ex = 1
    for j in range(1,display_rows+1):
        for i in range (1,display_cols+1):
            if curr_ex > m:
                break

            # Copy the patch

            # Get the max value of the patch to normalize all examples
            max_val = max(abs(X[curr_ex-1, :]))
            rows = pad + (j - 1) * (example_height + pad) + np.array(range(example_height))
            print(rows)
            print("----")
            cols = pad + (i - 1) * (example_width  + pad) + np.array(range(example_width ))
            print(cols)
            # Basic (vs. advanced) indexing/slicing is necessary so that we look can assign
            #   values directly to display_array and not to a copy of its subarray.
            #   from stackoverflow.com/a/7960811/583834 and
            #   bytes.com/topic/python/answers/759181-help-slicing-replacing-matrix-sections
            # Also notice the order="F" parameter on the reshape call - this is because python's
            #   default reshape function uses "C-like index order, with the last axis index
            #   changing fastest, back to the first axis index changing slowest" i.e.
            #   it first fills out the first row/the first index, then the second row, etc.
            #   matlab uses "Fortran-like index order, with the first index changing fastest,
            #   and the last index changing slowest" i.e. it first fills out the first column,
            #   then the second column, etc. This latter behaviour is what we want.
            #   Alternatively, we can keep the deault order="C" and then transpose the result
            #   from the reshape call.
            display_array[rows[0]:rows[-1]+1 , cols[0]:cols[-1]+1] = np.reshape(X[curr_ex-1, :], (example_height, example_width), order="F") / max_val
            curr_ex += 1

        if curr_ex > m:
            break

    # Display Image
    h = plt.imshow(display_array, vmin=-1, vmax=1)

    # Do not show axis
    plt.axis('off')

    plt.show(block=False)

    return h, display_array
