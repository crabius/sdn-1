from ryu.base import app_manager
from ryu.controller import ofp_event
from ryu.controller.handler import MAIN_DISPATCHER
from ryu.controller.handler import set_ev_cls
from ryu.ofproto import ofproto_v1_0

#implement a simple switch that acts as a hub.
#when a packet comes in on a given interface x, 
#broadcast it out on all interfaces != x
class simple_switch(app_manager.RyuApp):
    "a simple switch that acts as a hub."
    OFP_VERSIONS = [ofproto_v1_0.OFP_VERSION]
    
    #constructor
    def __init__(self, *args, **kwargs):
        super(simple_switch, self).__init__(*args, **kwargs)

    #set_ev_cls tells us when this packet handler method should be invoked
    #we set it to EventOFPPacketIn, i.e we recieve a packet
    #MAIN_DISPATCHER tells us to call only after we have the whole packet
    @set_ev_cls(ofp_event.EventOFPPacketIn, MAIN_DISPATCHER)
    def packet_in_handler(self, ev):
        #ev.msg is a data structure that holds incoming openflow packet
        msg = ev.msg
        #msg.datapath is an object representing a datapath (switch)
        dp = msg.datapath
        #dp.ofproto and dp.ofproto_parser represent openflow protocol
        ofp = dp.ofproto
        ofp_parser = dp.ofproto_parser

        #OFPActionOutput is used with a packet_out message to specify
        #the switch port you want to send the packet out of
        #ofp.OFPP_FLOOD tells it to flood (send the packet out on all interfaces)
        actions = [ofp_parser.OFPActionOutput(ofp.OFPP_FLOOD)]

        data = None
        if msg.buffer_id == ofp.OFP_NO_BUFFER:
            data = msg.data
        
        #OFPPacketOut builds the packet_out message (outgoing packet)
        #datapath (switch) is our switch 
        #buffer_id is the switch buffer to send to? (Not sure about this)
        #in_port = port we are coming in from
        #actions specifies the actiosn we want to take (here it is flood)
        #data is the contents of the packet (here it is the incoming packet contents as we are just forwarding)
        out = ofp_parser.OFPPacketOut(
                datapath=dp, buffer_id=msg.buffer_id, in_port=msg.in_port,
                actions=actions, data=data)
        #send the message
        dp.send_msg(out)
