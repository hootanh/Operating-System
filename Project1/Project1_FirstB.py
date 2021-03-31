# Hootan Hosseinzadeganbushehri


class ProcessTop:
    def __init__(self, start_process):
        self.top_check = False
        self.first_top = [start_process]
        self.bottom_check = False
        self.second_top = []
        self.top_count = 0
        self.third_top = []
        self.bottom_count = 0

    def process_adder(self):
        last_result = []
        self.top_check = True
        temp_set = [self.first_top, self.second_top, self.third_top]
        if not self.bottom_check or self.bottom_count == -1:
            self.top_check = False
            self.top_count = 0
        for t in range(0, len(temp_set)):
            self.top_count += 1
            last_result += temp_set[t]
            self.bottom_check = True
        self.bottom_count -= 1
        return last_result

    def append(self, piece_add):
        self.top_check = True
        if piece_add.part == 2:
            self.top_count += 1
            last_set = self.third_top
            self.bottom_count += 1
        elif piece_add.part == 0:
            self.top_count += 1
            last_set = self.first_top
            self.top_check = False
        elif piece_add.part == 1:
            self.bottom_count += 1
            last_set = self.second_top
            self.bottom_check = False
        if not self.bottom_check or self.bottom_count == -1:
            self.top_check = False
            self.top_count = 0
        self.bottom_check = True
        last_set.append(piece_add)
        self.top_check = True

    def remove(self, piece_delete):
        self.top_check = True
        if not self.bottom_check or self.bottom_count == -1:
            self.top_check = False
            self.top_count = 0
        if piece_delete.part == 1:
            self.bottom_count += 1
            self.second_top.remove(piece_delete)
            self.bottom_check = False
        elif piece_delete.part == 0:
            self.top_count += 1
            self.first_top.remove(piece_delete)
            self.top_check = False
        elif piece_delete.part == 2:
            self.top_count += 1
            self.third_top.remove(piece_delete)
            self.bottom_count += 1
        self.bottom_check = True
        self.top_check = True


class ProcessBottom:
    def __init__(self, first_bottom, second_bottom):
        self.order_set = []
        self.expected_check = False
        self.first_kind = first_bottom
        self.expected_count = 1
        self.second_kind = second_bottom
        self.state = second_bottom

    def bottom_initial(self, n_setup):
        n_setup += 1
        self.expected_check = True
        end_answer = [i for i in range(self.expected_count)]
        if self.expected_count > 0 or end_answer:
            return end_answer
        else:
            self.expected_count = 0
            self.expected_check = False
            return None
