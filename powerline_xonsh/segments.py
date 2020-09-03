from powerline.theme import requires_segment_info


@requires_segment_info
def exec_time(pl, segment_info):
    """Return execution time of the last command

    Highlight group used: ``exec_time``
    """

    execution_time = getattr(segment_info.get("args", None), "execution_time", 0)

    if execution_time:
        return [{"contents": f"{execution_time:.2f}s", "highlight_groups": ["exec_time"]}]
