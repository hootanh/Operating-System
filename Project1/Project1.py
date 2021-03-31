# Hootan Hosseinzadeganbushehri


import sys
import Project1_First


def control_output(my_input):
    sys.stdout = open('output.txt', 'w')
    check_write = 0
    nxt_line = False
    read_c = 1
    for l_input in my_input:
        if 'in' == l_input[0]:
            current_p = Project1_First.FileProcess()
            if not nxt_line:
                read_c = 0
            else:
                check_write = 0
                print()
            nxt_line = True
            read_c += 1
            print(current_p.source_start.index, end=' ')
        elif 'de' == l_input[0]:
            check_new_setup = False
            for n in current_p.source_start.pos_set:
                if n.index != int(l_input[1]):
                    check_write += 1
                else:
                    check_new_setup = True
                    check_write = 0
                    break
            if not check_new_setup:
                print('-1', end=' ')
                check_write += 1
                current_r = False
            else:
                current_r = current_p.delete_process(int(l_input[1]))
                check_write -= 1
            if current_r is None or current_r:
                read_c += 1
                print(current_p.source_start.index, end=' ')
        elif '' == l_input[0]:
            check_write = 0
            continue
        elif 'to' == l_input[0]:
            current_p.latency_run()
            read_c = 0
            print(current_p.source_start.index, end=' ')
        elif 'cr' == l_input[0]:
            current_r = current_p.new_setup(int(l_input[1]))
            if current_r is not None:
                read_c -= 1
                check_write -= 1
            else:
                check_write += 1
                print(current_p.source_start.index, end=' ')
        elif 'rl' == l_input[0]:
            current_r = current_p.process_flow(int(l_input[1]), int(l_input[2]))
            check_write = 0
            if current_r is not None:
                check_write -= 1
            else:
                check_write += 1
                print(current_p.source_start.index, end=' ')
        elif 'rq' == l_input[0]:
            current_r = current_p.develop_process(int(l_input[1]), int(l_input[2]))
            check_write = 0
            if current_r is not None:
                check_write -= 1
                read_c = 0
            else:
                check_write += 1
                print(current_p.source_start.index, end=' ')


def new_process():
    lines = []
    if len(sys.argv) > 1:
        in_file = open(sys.argv[1])
        while 1:
            in_line = in_file.readline()
            if in_line == '':
                break
            else:
                lines.append(in_line)
        my_list = [line.strip().split(' ') for line in lines]
        in_file.close()
    control_output(my_list)


if __name__ == '__main__':
    new_process()
