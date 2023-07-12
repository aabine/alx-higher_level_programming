import sys
from collections import defaultdict

""" Write a script that reads stdin line by line and computes metrics """

def compute_metrics():
    """
    Compute metrics based on the input received from the standard input.
    
    This function reads lines from the standard input and computes various metrics based on the information extracted from each line. The metrics computed are:
    - Total file size: The sum of the file sizes extracted from each line.
    - Status code counts: The number of occurrences of each status code extracted from each line.
    
    Parameters:
    None
    
    Returns:
    None
    
    Raises:
    KeyboardInterrupt: If the function is interrupted by the user (CTRL + C).
    """
    total_size = 0
    status_counts = defaultdict(int)
    line_count = 0

    try:
        for line in sys.stdin:
            line = line.strip()
            if line:
                line_count += 1

                # Parse the line and extract necessary information
                parts = line.split(' ')
                size = int(parts[-1])
                status_code = parts[-2]

                # Update metrics
                total_size += size
                status_counts[status_code] += 1

                # Print statistics every 10 lines
                if line_count % 10 == 0:
                    print("Total file size:", total_size)
                    for code in sorted(status_counts):
                        count = status_counts[code]
                        print("{}: {}".format(code, count))

    except KeyboardInterrupt:
        # Handle keyboard interruption (CTRL + C)
        print("Total file size:", total_size)
        for code in sorted(status_counts):
            count = status_counts[code]
            print("{}: {}".format(code, count))


if __name__ == "__main__":
    compute_metrics()
