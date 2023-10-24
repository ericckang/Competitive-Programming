#Author: Eric Kang
#It is not ok to share my code anonymously for educational purposes
def main():
    def min_weight_of_heaviest_box(total_items, total_boxes, item_weights):
        # The heaviest single item.
        heaviest_single_item = max(item_weights)

        # All items in one box.
        weight_all_items = sum(item_weights)

        # Establishing the binary search boundaries.
        lower_bound = heaviest_single_item
        upper_bound = weight_all_items

        # Performing the binary search.
        while lower_bound < upper_bound:
            current_guess = (lower_bound + upper_bound) // 2

            # Variables for the current sum of weights and the number of boxes used.
            current_sum = 0
            boxes_used = 1

            # Check feasibility of current guess by trying to pack boxes.
            for weight in item_weights:
                current_sum += weight
                if current_sum > current_guess:
                    # Need another box for the remaining items.
                    boxes_used += 1
                    current_sum = weight  # The current item starts a new box.

            # Adjusting the binary search boundaries based on feasibility.
            if boxes_used > total_boxes:
                lower_bound = current_guess + 1  # Current guess was too low, so go higher.
            else:
                upper_bound = current_guess  # Current guess was sufficient, so go lower or stay.

        # When lower_bound meets upper_bound, we found our minimum possible weight.
        return lower_bound

    total_items, total_boxes = map(int, input().split())
    item_weights = list(map(int, input().split()))

    print(min_weight_of_heaviest_box(total_items, total_boxes, item_weights))

if __name__ == "__main__":
    main()
