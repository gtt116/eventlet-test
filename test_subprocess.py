"""
Test eventlet subprocess if can block all greenlets.
"""
import eventlet
# Since we monkey_patch the select module, so subprocess will not block all
# greenlets. If you commet the line here, it will block forever.
eventlet.monkey_patch(select=False)

from nova import utils


def work():
    while True:
        print '.'
        eventlet.sleep(1)

eventlet.spawn_n(work)
eventlet.sleep(0)

print utils.execute('cat', '/dev/random')
