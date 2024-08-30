define print_thread_info
    echo \n*** Thread $threadnum ***\n
    info thread
    thread $threadnum
    frame 0
    while ($frame_num < $bt_num)
        echo \n# Frame $frame_num\n
        info locals
        info args
        up-silently
        set $frame_num = $frame_num + 1
    end
end

define print_all_threads_info
    set $threadnum = 1
    set $frame_num = 0
    set $bt_num = 0
    while ($threadnum <= $num_threads)
        thread $threadnum
        bt  # Get the number of frames for this thread
        set $bt_num = $_s
        print_thread_info
        set $threadnum = $threadnum + 1
    end
end

set $num_threads = 0
info threads
set $num_threads = $_s

print_all_threads_info

