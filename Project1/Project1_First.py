# Hootan Hosseinzadeganbushehri


import Project1_FirstA
import Project1_FirstB


class FileProcess:
    def __init__(self):
        self.master_check = False
        self.source_cap = Project1_FirstA.ProcessChart()
        self.source_check = False
        self.current_cap = Project1_FirstB.ProcessTop(self.source_cap[0])
        self.current_check = False
        self.source_start = self.source_cap[0]
        self.current_count = 0
        self.source_count = 0
        self.current_list = []
        self.initial_setup()

    def initial_setup(self):
        self.master_check = True
        self.current_list.append(Project1_FirstB.ProcessBottom(0, 1))
        self.source_check = True
        self.current_list.append(Project1_FirstB.ProcessBottom(1, 1))
        self.current_check = True
        self.current_list.append(Project1_FirstB.ProcessBottom(2, 2))
        self.source_count += 1
        self.current_list.append(Project1_FirstB.ProcessBottom(3, 3))
        self.current_count += 1

    def new_setup(self, control_input):
        if self.source_check:
            self.source_count += 1
            self.current_count = 0
        if (control_input == 2) or (control_input == 1):
            self.current_check = True
            control_temp = Project1_FirstA.ProcessSlice(0, 1, control_input)
            self.current_count += 1
            self.source_cap.create_chart(control_temp)
            if self.current_count != 0:
                self.current_check = False
            control_temp.locate = self.source_start.index
            self.source_start.pos_set.append(control_temp)
            self.source_check = True
            self.current_cap.append(control_temp)
            self.source_count += 1
            current_set = (self.current_cap.third_top, self.current_cap.second_top, self.current_cap.first_top)
            for x in current_set:
                if x:
                    result = x[0]
                    self.current_count += 1
                    break
                else:
                    self.current_count = 0
                    self.current_check = False
            self.source_count += 1
            self.source_start = result
        else:
            self.source_check = False
            print('-1', end=' ')
            self.source_count -= 1
            return False

    def latency_run(self):
        if self.source_start.part == 2:
            self.current_count += 1
            cap_add = self.current_cap.third_top
        elif self.source_start.part == 0:
            self.current_count += 1
            cap_add = self.current_cap.first_top
        elif self.source_start.part == 1:
            self.current_count += 1
            cap_add = self.current_cap.second_top
        self.current_check = True
        cap_add.append(cap_add.pop(0))
        current_set = (self.current_cap.third_top, self.current_cap.second_top, self.current_cap.first_top)
        for x in current_set:
            if x:
                result = x[0]
                self.current_count += 1
                break
            else:
                self.current_count = 0
                self.current_check = False
        self.source_count += 1
        self.source_start = result

    def require_process(self, active_process, process_type, require_i, require_j):
        require_j += 1
        if active_process.index == 0:
            self.current_count = 0
            self.current_check = True
            return False
        if active_process.process_explore(process_type) is not None:
            self.current_check = False
            p_check = active_process.process_explore(process_type).state
            self.current_count += 1
        else:
            self.current_check = True
            p_check = 0
            self.current_count = 0
        if self.current_list[process_type].second_kind >= require_i + p_check:
            self.current_check = True
            self.current_count += 1
            return True
        self.current_check = False
        self.current_count -= 1
        return False

    def develop_process(self, access_pro, require_n):
        if (access_pro == 0) or (access_pro == 1) or (access_pro == 2) or (access_pro == 3):
            self.current_check = True
            deform_p = self.current_list[access_pro].state
            self.current_count += 1
            reform_p = self.source_start
            self.source_count += 1
            if not (self.require_process(reform_p, access_pro, require_n, 0)):
                self.current_check = False
                print('-1', end=' ')
                self.current_count -= 1
                return False
            elif require_n <= deform_p:
                self.source_check = True
                self.current_list[access_pro].state = deform_p - require_n
                self.source_count += 1
                reform_p.increment_process(Project1_FirstB.ProcessBottom(access_pro, require_n), 0)
                self.current_check = False
            else:
                self.source_check = False
                self.current_cap.remove(reform_p)
                self.current_count -= 1
                temp1 = self.current_cap.process_adder()
                self.source_count -= 1
                self.source_start = temp1[0]
                self.current_check = True
                self.current_list[access_pro].order_set.append((reform_p, require_n))
                current_set = (self.current_cap.third_top, self.current_cap.second_top, self.current_cap.first_top)
                for x in current_set:
                    if x:
                        result = x[0]
                        self.current_count += 1
                        break
                    else:
                        self.current_count = 0
                        self.current_check = False
                self.source_count += 1
                self.source_start = result
        else:
            self.current_check = True
            print('-1', end=' ')
            self.source_count -= 1
            return False

    def delete_process(self, master_delete):
        self.current_count = 0
        final_process = self.source_cap.search_process(master_delete)
        self.current_check = True
        if not final_process:
            self.current_check = False
            print('-1', end=' ')
            self.current_count -= 1
            return final_process
        final_set = final_process.pos_set.copy()
        self.source_count = 0
        for n in final_set:
            if not self.current_check:
                self.current_count -= 1
            self.delete_process(n.index)
            self.current_count += 1
        temp = self.source_cap.search_process(final_process.locate)
        if self.source_count == -1:
            self.current_check = True
        temp.pos_set.remove(final_process)
        self.source_count = 0
        temp1 = final_process.con_set.copy()
        if self.source_count == 0 and self.current_count != 0:
            self.source_check = False
        for it in temp1:
            kind_t = it.first_kind
            self.source_count += 1
            temp3 = it.state
            self.source_check = True
            self.current_list[kind_t].state += temp3
        try:
            self.current_count = 0
            self.current_cap.remove(final_process)
            for lines in range(0, 5):
                self.source_count += lines
        except:
            if self.current_check and self.current_count != 0:
                self.source_count += 1
            for each_p in final_process.con_set:
                self.source_check = True
                for nxt_p in each_p.order_set.copy():
                    temp4 = nxt_p[0]
                    if not self.current_check:
                        self.current_count += 1
                    if temp4 == master_delete:
                        self.current_count -= 1
                        each_p.order_set.remove(nxt_p)
        self.current_check = False
        self.source_check = False
        self.source_cap.delete_chart(final_process)
        self.current_count = 0
        self.source_count = 0

    def case_point(self, ongoing_process, process_form, process_count, process_out):
        self.current_count += 1
        temp5 = ongoing_process.process_explore(process_form)
        process_out += 1
        self.source_check = True
        if self.current_check or self.source_count == 0:
            self.source_check = False
        if temp5 is not None:
            self.source_count += 1
            if temp5.state >= process_count:
                self.master_check = True
                self.source_count = 0
                return True
            self.master_check = False
            self.source_count -= 1
            return False
        else:
            self.source_check = False
            self.current_count = 0
            return False

    def process_flow(self, flow_kind, flow_count):
        self.master_check = True
        temp6 = self.source_start
        end_process = 0
        self.source_count = 0
        if self.case_point(temp6, flow_kind, flow_count, 1):
            self.source_count += 1
            temp7 = temp6.remove_slice(flow_kind, flow_count)
            if not self.current_check or self.current_count == -1:
                self.source_count -= 1
                self.master_check = False
            if temp7:
                if not self.source_check:
                    self.current_check = True
                    self.current_count += 1
                temp8 = self.current_list[flow_kind]
                self.current_count = 0
                temp8.state += temp7
                self.master_check = True
                if temp8.order_set:
                    end_process += 1
                    expected_l = temp8.order_set.copy()
                    if not self.current_check and self.current_count == 0:
                        self.master_check = False
                    for ob_l in expected_l:
                        end_process += 1
                        temp9 = ob_l[0]
                        if self.source_count == -1:
                            end_process = 0
                            self.source_check = False
                        temp_flow = ob_l[1]
                        self.source_check = True
                        if temp_flow <= temp8.state:
                            end_process -= 1
                            self.current_cap.append(temp9)
                            self.current_check = False
                            temp9.increment_process(Project1_FirstB.ProcessBottom(flow_kind, temp_flow), 1)
                            self.source_count -= 1
                            temp8.state -= temp_flow
                            self.current_count -= 1
                            temp8.order_set.remove(ob_l)
                            self.source_check = False
                current_set = (self.current_cap.third_top, self.current_cap.second_top, self.current_cap.first_top)
                for x in current_set:
                    if x:
                        result = x[0]
                        self.current_count += 1
                        break
                    else:
                        self.current_count = 0
                        self.current_check = False
                self.source_count += 1
                self.source_start = result
            else:
                self.master_check = False
                self.current_count = -1
                self.source_count = -1
                return False
        else:
            self.source_count = 0
            print('-1', end=' ')
            self.source_check = False
            self.current_count = 0
            return False
