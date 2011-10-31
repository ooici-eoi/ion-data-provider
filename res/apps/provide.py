#!/usr/bin/env python

"""

"""
from twisted.internet import defer, reactor

from ion.core.process import process
from ion.core import ioninit
from ion.core.ioninit import container_instance
from ion.integration.eoi.agent.java_agent_wrapper import JavaAgentWrapper as jaw

import logging
import ion.util.ionlog

log = ion.util.ionlog.getLogger(__name__)

jaw_instance = None

@defer.inlineCallbacks
def run():
    log.debug("Getting dataset_id")
    try:
        ds_id = ioninit.cont_args['dataset_id']
    except Exception, ex:
        raise RuntimeError("Could not find dataset_id argument", str(ex))

    vals = container_instance.proc_manager.process_registry.kvs.values()
    log.debug("Finding JavaAgentWrapper instance")
    for v in vals:
        if isinstance(v,jaw):
            jaw_instance=v
            break

    if jaw_instance is None:
        raise RuntimeError("jaw_instance is None")

    log.debug("Found JavaAgentWrapper instance!")
    log.debug("Initiating update")
    done = yield jaw_instance._update_request(ds_id,None)

    yield container_instance.terminate()

    reactor.stop()
    global exit_status
    exit_status = 0

run()

