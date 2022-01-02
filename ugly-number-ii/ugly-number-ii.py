class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly_number_list = [1]

        # counter to represent whether 2, 3, or 5 was used to pick the last ugly number
        num_2, num_3, num_5 = 0, 0, 0

        while len(ugly_number_list) != n:
            min_all_considered = min(ugly_number_list[num_2] * 2, ugly_number_list[num_3] * 3, ugly_number_list[num_5] * 5)

            if min_all_considered == ugly_number_list[num_2] * 2:
                num_2 += 1

            if min_all_considered == ugly_number_list[num_3] * 3:
                num_3 += 1

            if min_all_considered == ugly_number_list[num_5] * 5:
                num_5 += 1


            ugly_number_list.append(min_all_considered)

        return ugly_number_list[n-1]
