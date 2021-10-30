from opentrons import protocol_api

metadata = {
    'apiLevel': '2.10',
    'author': 'Cacti biochemist'
}

def run(protocol: protocol_api.ProtocolContext):
    plate = protocol.load_labware('corning_96_wellplate_360ul_flat', 1)
    tiprack_1 = protocol.load_labware('opentrons_96_tiprack_300ul', 2)
    p300 = protocol.load_instrument('p300_single', 'left', tip_racks=[tiprack_1])

    p300.transfer(100, plate['A1'], plate['A1'])
    p300.transfer(120, plate['A2'], plate['B2'])
    p300.transfer(140, plate['A3'], plate['B3'])
    p300.transfer(160, plate['A4'], plate['B4'])
    p300.transfer(180, plate['A5'], plate['B5'])
    p300.transfer(200, plate['A6'], plate['B6'])
    p300.transfer(220, plate['A7'], plate['B7'])
    p300.transfer(240, plate['A8'], plate['B8'])
    p300.transfer(260, plate['A9'], plate['B9'])
    p300.transfer(280, plate['A10'], plate['B10'])
    p300.transfer(300, plate['A11'], plate['B11'])