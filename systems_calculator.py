import math

def memory_location_calculator():
    print('How many bits are the instructions?')
    instructions = int(input())
    print('How many bits in opcode?')
    opcode = int(input())
    address = instructions - opcode
    memory_locations = 2**address
    print('There are ' + str(memory_locations) + ' memory locations that can be referenced by these instructions')

def instruction_length_calculator():
    print('How many memory locations are there?')
    memory_locations = int(input())
    print('What is the bit length of the opcode?')
    opcode = int(input())
    address = math.log2(memory_locations) 
    instructions = opcode + address
    print('The instructions are of size ' + str(int(instructions)) + ' bits')

def opcode_length_calculator():
    print('What is the bit length of the instructions?')
    instructions = int(input())
    print('How many memory locations are there?')
    memory_locations = int(input())
    address = math.log2(memory_locations) 
    opcode = instructions - address
    print('The opcode is of length ' + str(int(opcode)) + ' bits')

def location_in_memory_calculator():
    print('What base are the instructions written in? (Enter 8 for Base8)')
    base = int(input())
    if base == 8:
        print("What is the instruction number?")
        instruction = input()        
        print("What is the bit length of the opcode?")
        opcode = int(input())
        digit = 3
        leftmost_digits_amount = int(opcode / digit)
        memory_represented_instruction = instruction[leftmost_digits_amount:]
        print('The location in memory to be accessed is ' + memory_represented_instruction)

def opcode_represented_calculator():
    print('What base are the instructions written in? (Enter 8 for Base8)')
    base = int(input())
    if base == 8:
        print("What is the instruction number?")
        instruction = input()        
        print("What is the bit length of the opcode?")
        opcode = int(input())
        digit = 3
        leftmost_digits_amount = int(opcode / digit)
        opcode_represented_instruction = instruction[:leftmost_digits_amount]
        print('The opcode is represented by ' + opcode_represented_instruction)

def memory_location_region_calculator():
    print('How many bits are the instructions?')
    instructions = int(input())
    print('How many bits in opcode?')
    opcode = int(input())
    print('How many bits in word?')
    word = int(input())
    address = instructions - opcode
    memory_locations = 2**address
    amount_of_data_in_locations = int(memory_locations * word)
    print('Do you need the answer given in bytes (Enter 1) or bits (Enter 2)?')
    answer = int(input())
    if answer == 1:
        print('The size of the region in main memory is ' + str(int(amount_of_data_in_locations / 8)))
    if answer == 2:
        print('The size of the region in main memory is ' + str(amount_of_data_in_locations))

def processes_calculator():
    print('How many processes admitted from "new" state and executing on system with a single CPU?')
    processes = int(input())
    print('How many processes make requests?')
    requesting_processes = int(input())
    remaining_processes = int(processes - requesting_processes)
    print(str(remaining_processes) + " processes will never be in the blocked state, they're either running or in the ready queue. \nSo smallest number of processes in ready queue is " + str(remaining_processes - 1) + " and this can happen if one of the processes is running on the CPU and all the processes with requests are blocked")
    print("It's possible for all " + str(requesting_processes) + " to be in ready queue waiting to be assigned to CPU, so blocked queue would be empty.")

def tuarnaround_time_calculator():
    print("How many processes are there? (Enter 2 for two)")
    number_of_processes = int(input())
    print("What's the service time of process 1? (Make sure it's smaller or the same as process 2)")
    process_1 = int(input())
    print("What's the service time of process 2?")
    process_2 = int(input())
    print("What's the time quantum")
    quantum = int(input())
    if process_1 < process_2:
        process_1_entry_time = 0
        process_1_exit_time = (process_1 * number_of_processes) - quantum
        process_2_entry_time = process_1_entry_time + quantum
        remaining_process_1 = ((process_1 - quantum) * number_of_processes) - quantum
        remaining_process_2 = (process_2 - quantum) - ((remaining_process_1 - quantum)/2)
        process_2_exit_time = process_1_exit_time + remaining_process_2
        turnaround = ((process_1_exit_time - process_1_entry_time) + (process_2_exit_time - process_2_entry_time)) / number_of_processes
        print("The turnaround time is: " + str(turnaround) + "time units.")

def mode_switch_calculator():
    print("How many programs are there? (Enter 2 for two)")
    number_of_programs = int(input())
    print("What's the service time of program 1?")
    program1 = int(input())
    print("What's the service time of program 2?")
    program_2 = int(input())
    print("What's the time quantum or slice time")
    quantum = int(input())
    mode_switch_number = 2
    print("Would you like to calculate from when program 1 (enter 1) finished running x times or program 2 (enter 2) finished running x times?")
    choice = int(input())
    if choice == 1:
        print("How much time did program 1 spend running on ther CPU?")
        program_1_time = int(input())
        switched_processes = (math.ceil(program_1_time/quantum) - 1) * 2
        mode_switches = switched_processes * mode_switch_number
        print("The number of mode switches due to interruprs by the time program 1 has spent " + str(program_1_time) + " times running on the CPU is " + str(int(mode_switches)) + ".")

def code_switch_calculator():
    print("What's the process size that's swapping into the hard disk? (in Mb)")
    process_size = float(input())
    print("What's the transfer rate of hard disk? (in Mb/s)")
    transfer_rate = float(input())
    print("Is the latency in μs (enter 1) or ms (enter 2)?")
    choice = int(input())
    if choice == 1:
        print("What's the latency in (in μs)?")
        latency = float(input()) / 1000
        swap_out_time = (process_size / transfer_rate) * 1000
        context_switch_swap_time = float(swap_out_time * 2) + (2 * latency)
        print("Total context switch swapping component time is " + str(context_switch_swap_time) + " ms")
    if choice == 2:
        print("What's the latency in (in ms)?")
        latency = float(input()) 
        swap_out_time = (process_size / transfer_rate) * 1000
        context_switch_swap_time = float(swap_out_time * 2) + (2 * latency)
        print("Total context switch swapping component time is " + str(context_switch_swap_time) + " ms")

def slowdown_factor_calculator():
    print("What's the process size? (in Mb)")
    process_size = float(input())
    print("What's the time in runs normally in? (in ms)")
    run_time = int(input())
    print("What's the average time between context switching? (in μs)")
    context_switch_time = float(input()) / 1000
    print("What's the time taken to transfer from disk (in Mb/s)")
    transfer_time = int(input())
    t_fast = float(run_time) + context_switch_time
    print(t_fast)
    t_slow = float(run_time) + context_switch_time + (2*(process_size/transfer_time)*1000)
    print(t_slow)
    slowdown_factor = t_slow / t_fast
    print("The slowdown factor is " + str(slowdown_factor))

def paging_calculator():
    print("What's the page size? (in bytes)")
    page_size = int(input())
    print("What's the frame size (in kB)")
    frame_size = int(input())
    bits = page_size * 8
    frames = 2 ** bits
    frame_size_bits = frame_size * 1024
    physical_memory = frame_size_bits * frames
    print("The amount of frames are " + str(frames) + " or 2^" + str(int(math.log(frames, 2))))
    print("The amount of physical memory that can be addressed is " + str(physical_memory) + " bytes or " + str((float(physical_memory)/1000000000)) + " gigabytes or " + str((float(physical_memory)/1000000000000)) + " terabytes")

def paging_internal_fragmentation_calculator():
    print("What's the page size? (in bytes)")
    page_size = int(input())
    print("What's the process size (in bytes)")
    process_size = int(input())
    pages = float("%0.2f" % (process_size/page_size))
    pages_round_up = math.ceil(pages)
    frac, whole = math.modf(pages)
    internal_fragmentation = page_size - math.ceil(frac * page_size)
    print("There are " + str(pages_round_up) + " pages required")
    print("The internal fragmentation is " + str(internal_fragmentation) + " bytes")
    print("Best case fragmentation is a full frame with no fragmentation")
    print("Worst case fragmentation is a frame with 1 byte")

def eat_calculator():
    print("What's the base memory time? (in ns)")
    base_memory_time = int(input(220))
    print("What's the average page-fault service time (in ms)")
    page_fault = int(input(7)) * 1000000
    print("What's the page-fault rate (in ms)")
    p = float(input(1.1x(10^-5))
    a = base_memory_time
    s = page_fault
    eat = a + (p * s)
    slowdown_factor = eat / base_memory_time
    print("The effective access time is " + str(eat) + " ns")
    print("The slowdown factor is " + str(slowdown_factor))



print('What do you need to find?')
print('-------------------------')
print('1 - Number of memory locations from instructions and opcode?')
print('2 - Bit length of instructions from number of memory locations and opcode?')
print('3 - Bit length of opcode from length of instructions and number of memory locations?')
print('4 - Location in memory of instruction to be accessed by processor from opcode length and instruction?')
print('5 - Opcode represented in instruction from opcode length and instruction?')
print('6 - Size of region in main memory that contains locations referenced in CPU instructions from instruction length, opcode length and word length')
print('7 - Assuming 5 state process model, minimum number of processes in ready and blocked states before any process terminates?')
print('8 - Average turnaround time from proccesses time and avergae turnaround time?')
print('9 - Number of times mode switches occur due to interrupts from time a program has spent x units running?')
print('10 - Context switch time with swapping')
print('11 - Slowdown factor calculator')
print('12 - Paging calculator')
print('13 - Paging internal fragmentation calculator')
print('14 - EAT calculator with one memory reference in every 1000 results in a page-fault')







choice = int(input())
if choice == 1:
    memory_location_calculator()
elif choice == 2:
    instruction_length_calculator()
elif choice == 3:
    opcode_length_calculator()
elif choice == 4:
    location_in_memory_calculator()
elif choice == 5:
    opcode_represented_calculator()
elif choice == 6:
    memory_location_region_calculator()
elif choice == 7:
    processes_calculator()
elif choice == 8:
    tuarnaround_time_calculator()
elif choice == 9:
    mode_switch_calculator()
elif choice == 10:
    code_switch_calculator()
elif choice == 11:
    slowdown_factor_calculator()
elif choice == 12:
    paging_calculator()
elif choice == 13:
    paging_internal_fragmentation_calculator()
elif choice == 14:
    eat_calculator()


