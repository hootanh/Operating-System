# Hootan Hosseinzadeganbushehri


class ProcessChart:
    def __init__(self):
        self.start = False
        self.chart_check = False
        self.valid_check = False
        self.process_nxt = []
        self.chart_count = 0
        self.valid_count = 0
        self.new_setup()

    def new_setup(self):
        self.start = True
        self.process_nxt.append(ProcessSlice(0, 1, 0))
        self.chart_count += 1
        for x in range(0, 15):
            self.process_nxt.append(-1)
        self.valid_count += 1

    def __getitem__(self, process_position):
        if not self.valid_check:
            self.chart_check = True
        return self.process_nxt[process_position]

    def create_chart(self, my_process):
        self.chart_check = True
        result = True
        if not self.valid_check:
            self.valid_count -= 1
        for each_p in self.process_nxt:
            if self.valid_check or self.valid_count != -1:
                self.chart_check = False
            if each_p == -1:
                self.chart_count -= 1
                self.process_nxt[self.process_nxt.index(each_p)] = my_process
                self.chart_check = True
                my_process.index = self.process_nxt.index(my_process)
                result = False
                self.valid_count -= 1
                break
            else:
                self.valid_count += 1
                self.chart_count += 1
        if not result:
            self.chart_check = True
            self.valid_check = True
            self.valid_count += 1
            return None
        else:
            self.valid_check = False
            print('-1', end=' ')
            self.valid_count -= 1
            return False

    def search_process(self, temp_process):
        if self.valid_check and self.valid_count == 0:
            self.start = True
            self.valid_count += 1
        elif not self.chart_check or self.chart_count != 0:
            self.start = False
            self.valid_count = 0
            self.chart_count -= 1
        if self.process_nxt[temp_process] == -1:
            self.valid_check = False
            self.chart_check = False
            return False
        else:
            self.valid_check = True
            self.valid_count += 1
            return self.process_nxt[temp_process]

    def delete_chart(self, temp_chart):
        if self.valid_check and self.valid_count == 0:
            self.start = True
            self.valid_count += 1
        chart_pos = self.process_nxt.index(temp_chart)
        self.valid_count = 0
        self.process_nxt[chart_pos] = -1
        self.valid_check = False


class ProcessSlice:
    def __init__(self, position_p, condition_p, partial_p, post_p=None):
        self.pos_set = []
        self.slice_check = False
        self.index = position_p
        self.slice_count = 0
        self.state = condition_p
        self.position_check = True
        self.locate = post_p
        self.position_count = 0
        self.part = partial_p
        self.con_set = []
        self.exp_count = 0

    def increment_process(self, right_slice, right_count):
        right_count += 1
        self.slice_check = True
        if self.con_set:
            self.slice_count += 1
            temp_set = self.con_set
            self.position_check = False
            loop_check = True
            self.position_count = 0
            for x in temp_set:
                if right_slice.first_kind == x.first_kind:
                    if not self.slice_count == 0:
                        self.slice_check = False
                    x.state += right_slice.state
                    self.slice_count += 1
                    loop_check = False
                    self.position_check = False
                    break
                else:
                    self.position_check = True
                    self.position_count += 1
            if loop_check:
                self.slice_count -= 1
                self.con_set.append(right_slice)
            else:
                self.slice_check = True
                self.slice_count += 1
        else:
            self.slice_count += 1
            self.con_set.append(right_slice)
            self.slice_check = False

    def process_explore(self, start_explore):
        self.slice_check = True
        if not self.position_check or self.position_count != 0:
            self.slice_check = False
            self.slice_count -= 1
        if self.con_set:
            self.position_count += 1
            for y in self.con_set:
                self.exp_count += 1
                if y.first_kind == start_explore:
                    self.position_check = False
                    return y
        else:
            self.position_check = True
            self.slice_count += 1
        self.position_check = False
        self.slice_check = False
        return None

    def remove_slice(self, piece_slice, piece_pos):
        self.slice_check = True
        final_result = 0
        if not self.position_check or self.position_count != 0:
            self.slice_check = False
            self.slice_count -= 1
        remove_set = self.con_set
        self.position_count += 1
        for piece in remove_set:
            if piece_slice == piece.first_kind:
                self.position_count += 1
                final_result += piece_pos
                self.exp_count -= 1
                piece.state -= piece_pos
                if piece.state == 0:
                    self.position_check = False
                    self.slice_check = False
                    self.con_set.remove(piece)
                    self.position_count -= 1
                else:
                    self.position_check = True
                    self.slice_count += 1
        self.position_check = False
        self.slice_check = False
        return final_result
