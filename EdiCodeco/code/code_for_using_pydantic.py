from __future__ import annotations

from enum import Enum
from typing import List, Optional, Union

from pydantic import AnyUrl, AwareDatetime, BaseModel, Field, RootModel, constr


class Address(BaseModel):
    addressCountry: Optional[str] = Field(
        None, description='The country. For example, Spain'
    )
    addressLocality: Optional[str] = Field(
        None,
        description='The locality in which the street address is, and which is in the region',
    )
    addressRegion: Optional[str] = Field(
        None,
        description='The region in which the locality is, and which is in the country',
    )
    district: Optional[str] = Field(
        None,
        description='A district is a type of administrative division that, in some countries, is managed by the local government',
    )
    postOfficeBoxNumber: Optional[str] = Field(
        None,
        description='The post office box number for PO box addresses. For example, 03578',
    )
    postalCode: Optional[str] = Field(
        None, description='The postal code. For example, 24004'
    )
    streetAddress: Optional[str] = Field(None, description='The street address')
    streetNr: Optional[str] = Field(
        None, description='Number identifying a specific property on a public street'
    )


class ContainerClass(Enum):
    Continental = 'Continental'
    Export = 'Export'
    Import = 'Import'
    Remain_on_board = 'Remain on board'
    Shifter = 'Shifter'
    Transhipment = 'Transhipment'


class ContainerIsoCode(Enum):
    Dime_coated_tank = 'Dime coated tank'
    Epoxy_coated_tank = 'Epoxy coated tank'
    IMO1 = 'IMO1'
    IMO2 = 'IMO2'
    IMO3 = 'IMO3'
    Pressurized_tank = 'Pressurized tank'
    Refrigerated_tank = 'Refrigerated tank'
    Semi_refrigerated = 'Semi-refrigerated'
    Stainless_steel_tank = 'Stainless steel tank'
    Nonworking_reefer_container_40_ft = 'Nonworking reefer container 40 ft'
    Box_pallet = 'Box pallet'
    Europallet = 'Europallet'
    Scandinavian_pallet = 'Scandinavian pallet'
    Trailer = 'Trailer'
    Nonworking_reefer_container_20_ft = 'Nonworking reefer container 20 ft'
    Exchangeable_pallet = 'Exchangeable pallet'
    Semi_trailer = 'Semi-trailer'
    Tank_container_20_ft_ = 'Tank container 20 ft.'
    Tank_container_30_ft_ = 'Tank container 30 ft.'
    Tank_container_40_ft_ = 'Tank container 40 ft.'
    Container_IC_20_ft_ = 'Container IC 20 ft.'
    Container_IC_30_ft_ = 'Container IC 30 ft.'
    Container_IC_40_ft_ = 'Container IC 40 ft.'
    Refrigerator_tank_20_ft_ = 'Refrigerator tank 20 ft.'
    Refrigerator_tank_30_ft_ = 'Refrigerator tank 30 ft.'
    Refrigerator_tank_40_ft_ = 'Refrigerator tank 40 ft.'
    Tank_container_IC_20_ft_ = 'Tank container IC 20 ft.'
    Tank_container_IC_30_ft_ = 'Tank container IC 30 ft.'
    Tank_container_IC_40_ft_ = 'Tank container IC 40 ft.'
    Refrigerator_tank_IC_20_ft_ = 'Refrigerator tank IC 20 ft.'
    Refrigerator_tank_IC_40_ft_ = 'Refrigerator tank IC 40 ft.'
    Movable_case__L___6_15m = 'Movable case: L < 6,15m'
    Movable_case__6_15m___L___7_82m = 'Movable case: 6,15m < L < 7,82m'
    Movable_case__7_82m___L___9_15m = 'Movable case: 7,82m < L < 9,15m'
    Movable_case__9_15m___L___10_90m = 'Movable case: 9,15m < L < 10,90m'
    Movable_case__10_90m___L___13_75m = 'Movable case: 10,90m < L < 13,75m'
    Totebin = 'Totebin'
    Temperature_controlled_container_20_ft = 'Temperature controlled container 20 ft'
    Temperature_controlled_container_40_ft = 'Temperature controlled container 40 ft'


class FunctionCode(Enum):
    Cancellation = 'Cancellation'
    Addition = 'Addition'
    Deletion = 'Deletion'
    Change = 'Change'
    Replace = 'Replace'
    Confirmation = 'Confirmation'
    Duplicate = 'Duplicate'
    Status = 'Status'
    Original = 'Original'
    Not_found = 'Not found'
    Response = 'Response'
    Not_processed = 'Not processed'
    Request = 'Request'
    Advance_notification = 'Advance notification'
    Reminder = 'Reminder'
    Proposal = 'Proposal'
    Cancel__to_be_reissued = 'Cancel, to be reissued'
    Reissue = 'Reissue'
    Seller_initiated_change = 'Seller initiated change'
    Replace_heading_section_only = 'Replace heading section only'
    Replace_item_detail_and_summary_only = 'Replace item detail and summary only'
    Final_transmission = 'Final transmission'
    Transaction_on_hold = 'Transaction on hold'
    Delivery_instruction = 'Delivery instruction'
    Forecast = 'Forecast'
    Delivery_instruction_and_forecast = 'Delivery instruction and forecast'
    Not_accepted = 'Not accepted'
    Accepted__with_amendment_in_heading_section = (
        'Accepted, with amendment in heading section'
    )
    Accepted_without_amendment = 'Accepted without amendment'
    Accepted__with_amendment_in_detail_section = (
        'Accepted, with amendment in detail section'
    )
    Copy = 'Copy'
    Approval = 'Approval'
    Change_in_heading_section = 'Change in heading section'
    Accepted_with_amendment = 'Accepted with amendment'
    Retransmission = 'Retransmission'
    Change_in_detail_section = 'Change in detail section'
    Reversal_of_a_debit = 'Reversal of a debit'
    Reversal_of_a_credit = 'Reversal of a credit'
    Reversal_for_cancellation = 'Reversal for cancellation'
    Request_for_deletion = 'Request for deletion'
    Finishing_closing_order = 'Finishing/closing order'
    Confirmation_via_specific_means = 'Confirmation via specific means'
    Additional_transmission = 'Additional transmission'
    Accepted_without_reserves = 'Accepted without reserves'
    Accepted_with_reserves = 'Accepted with reserves'
    Provisional = 'Provisional'
    Definitive = 'Definitive'
    Accepted__contents_rejected = 'Accepted, contents rejected'
    Settled_dispute = 'Settled dispute'
    Withdraw = 'Withdraw'
    Authorisation = 'Authorisation'
    Proposed_amendment = 'Proposed amendment'
    Test = 'Test'


class Type(Enum):
    Point = 'Point'


class Location(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[float] = Field(..., min_length=2)
    type: Type


class Coordinate(RootModel[List[float]]):
    root: List[float]


class Type1(Enum):
    LineString = 'LineString'


class Location1(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[Coordinate] = Field(..., min_length=2)
    type: Type1


class Type2(Enum):
    Polygon = 'Polygon'


class Location2(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[Coordinate]]
    type: Type2


class Type3(Enum):
    MultiPoint = 'MultiPoint'


class Location3(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[float]]
    type: Type3


class Type4(Enum):
    MultiLineString = 'MultiLineString'


class Location4(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[Coordinate]]
    type: Type4


class Type5(Enum):
    MultiPolygon = 'MultiPolygon'


class Location5(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[List[Coordinate]]]
    type: Type5


class OperationType(Enum):
    Place_of_terms_of_delivery = 'Place of terms of delivery'
    Payment_place = 'Payment place'
    Goods_receipt_place = 'Goods receipt place'
    Place_of_departure = 'Place of departure'
    Place_of_delivery = 'Place of delivery'
    Place_of_destination = 'Place of destination'
    Place_port_of_loading = 'Place/port of loading'
    Place_of_acceptance = 'Place of acceptance'
    Place_port_of_discharge = 'Place/port of discharge'
    Port_of_discharge = 'Port of discharge'
    Place_of_transhipment = 'Place of transhipment'
    Location_of_goods = 'Location of goods'
    Place_of_transfer_responsibility = 'Place of transfer responsibility'
    Place_of_transfer_of_ownership = 'Place of transfer of ownership'
    Border_crossing_place = 'Border crossing place'
    Warehouse = 'Warehouse'
    Factory_plant = 'Factory/plant'
    Place_of_ultimate_destination_of_goods = 'Place of ultimate destination of goods'
    Terms_of_sale_place = 'Terms of sale place'
    Customs_office_of_clearance = 'Customs office of clearance'
    Port_of_release = 'Port of release'
    Port_of_entry = 'Port of entry'
    Country = 'Country'
    City = 'City'
    Country_of_origin = 'Country of origin'
    Country_of_destination_of_goods = 'Country of destination of goods'
    Railway_station = 'Railway station'
    Country_of_source = 'Country of source'
    Building = 'Building'
    Beginning_of_chargeable_section = 'Beginning of chargeable section'
    Baseport_of_discharge = 'Baseport of discharge'
    Baseport_of_loading = 'Baseport of loading'
    Country_of_exportation_despatch = 'Country of exportation/despatch'
    Country_of_ultimate_destination = 'Country of ultimate destination'
    Country_of_last_consignment = 'Country of last consignment'
    Country_of_first_destination = 'Country of first destination'
    Country_of_production = 'Country of production'
    Country_of_trading = 'Country of trading'
    Customs_office_of_entry = 'Customs office of entry'
    Customs_office_of_exit = 'Customs office of exit'
    Place_of_Customs_examination = 'Place of Customs examination'
    Place_of_authentication_of_document = 'Place of authentication of document'
    Customs_office_of_destination__transit_ = 'Customs office of destination (transit)'
    Region_of_despatch = 'Region of despatch'
    Region_of_destination = 'Region of destination'
    Region_of_production = 'Region of production'
    Country_of_transit = 'Country of transit'
    Customs_office_of_transit = 'Customs office of transit'
    Country_of_invalid_transit_guarantee = 'Country of invalid transit guarantee'
    Country_of_destination__transit_ = 'Country of destination (transit)'
    Charge_and_freight_due_from = 'Charge and freight due from'
    Manufacturing_department = 'Manufacturing department'
    Charges_and_freight_payable_to = 'Charges and freight payable to'
    End_of_chargeable_section = 'End of chargeable section'
    Place_of_payment = 'Place of payment'
    Full_track_loading_or_unloading = 'Full track loading or unloading'
    Place_of_arrival = 'Place of arrival'
    Next_port_of_call = 'Next port of call'
    On_carriage_port = 'On-carriage port'
    First_optional_place_of_discharge = 'First optional place of discharge'
    Express_railway_station = 'Express railway station'
    Mixed_cargo_railway_station = 'Mixed cargo railway station'
    Second_optional_place_of_discharge = 'Second optional place of discharge'
    Next_non_discharge_port_of_call = 'Next non-discharge port of call'
    Third_optional_place_of_discharge = 'Third optional place of discharge'
    Reconsolidation_point = 'Reconsolidation point'
    Fourth_optional_place_of_discharge = 'Fourth optional place of discharge'
    Bill_of_lading_release_office = 'Bill of lading release office'
    Transhipment_excluding_this_place = 'Transhipment excluding this place'
    Transhipment_limited_to_this_place = 'Transhipment limited to this place'
    Original_port_of_loading = 'Original port of loading'
    First_port_of_call___non_discharging = 'First port of call - non-discharging'
    First_port_of_call___discharging = 'First port of call - discharging'
    Place_port_of_first_entry = 'Place/port of first entry'
    Place_of_despatch = 'Place of despatch'
    Fifth_optional_place_of_discharge = 'Fifth optional place of discharge'
    Pre_carriage_port = 'Pre-carriage port'
    Place_of_delivery__by_on_carriage_ = 'Place of delivery (by on carriage)'
    Transport_contract_place_of_acceptance = 'Transport contract place of acceptance'
    Transport_contract_place_of_destination = 'Transport contract place of destination'
    Country_of_valid_transit_guarantee = 'Country of valid transit guarantee'
    Place_port_of_conveyance_initial_arrival = (
        'Place/port of conveyance initial arrival'
    )
    Place_of_receipt = 'Place of receipt'
    Place_of_registration = 'Place of registration'
    Place_location_where_special_treatments_have_happened_or_must_happen = (
        'Place/location where special treatments have happened or must happen'
    )
    Place_of_document_issue = 'Place of document issue'
    Routing = 'Routing'
    Station_of_application_of_additional_costs = (
        'Station of application of additional costs'
    )
    Place_of_lodgement_of_documents = 'Place of lodgement of documents'
    Optional_place_of_discharge = 'Optional place of discharge'
    Place_of_empty_equipment_despatch = 'Place of empty equipment despatch'
    Place_of_empty_equipment_return = 'Place of empty equipment return'
    Place_port_of_warehouse_entry = 'Place/port of warehouse entry'
    Country_of_first_sale = 'Country of first sale'
    Country_of_purchase = 'Country of purchase'
    Place_of_transfer = 'Place of transfer'
    Place_of_deconsolidation = 'Place of deconsolidation'
    Place_of_consumption = 'Place of consumption'
    Region_of_origin = 'Region of origin'
    Place_of_consolidation = 'Place of consolidation'
    Rate_combination_point = 'Rate combination point'
    Place_of_prolongation_decision_of_delivery_delay = (
        'Place of prolongation decision of delivery delay'
    )
    Recharging_place_location = 'Recharging place/location'
    Customs_office_of_despatch = 'Customs office of despatch'
    Country_of_despatch = 'Country of despatch'
    Customs_office_of_export = 'Customs office of export'
    Free_zone_of_export = 'Free zone of export'
    Region_of_export_despatch = 'Region of export/despatch'
    Customs_office_of_departure = 'Customs office of departure'
    Customs_office_of_transit_guarantee = 'Customs office of transit guarantee'
    Country_of_transhipment = 'Country of transhipment'
    Country_of_sale = 'Country of sale'
    Customs_office_of_destination = 'Customs office of destination'
    Wagon_load_railway_station = 'Wagon-load railway station'
    Siding = 'Siding'
    Last_place_port_of_call_of_conveyance = 'Last place/port of call of conveyance'
    Country_of_previous_Customs_procedure = 'Country of previous Customs procedure'
    Customs_office_of_registration_of_previous_Customs_declaration = (
        'Customs office of registration of previous Customs declaration'
    )
    Participant_sender_location = 'Participant sender location'
    Wage_negotiation_district = 'Wage negotiation district'
    Place_of_ultimate_destination_of_conveyance = (
        'Place of ultimate destination of conveyance'
    )
    Place_of_loading_of_empty_equipment = 'Place of loading of empty equipment'
    Place_of_discharge_of_empty_equipment = 'Place of discharge of empty equipment'
    Region_of_delivery = 'Region of delivery'
    Petroleum_warehouse = 'Petroleum warehouse'
    Place_of_entry__Customs_ = 'Place of entry (Customs)'
    Living_animals_care_place = 'Living animals care place'
    Re_icing_place = 'Re-icing place'
    Weighting_place = 'Weighting place'
    Marshalling_yard = 'Marshalling yard'
    Shopping_station = 'Shopping station'
    Loading_dock = 'Loading dock'
    Port_connection = 'Port connection'
    Place_of_expiry = 'Place of expiry'
    Place_of_negotiation = 'Place of negotiation'
    Claims_payable_place = 'Claims payable place'
    Documentary_credit_available_in = 'Documentary credit available in'
    Stowage_cell = 'Stowage cell'
    For_transportation_to = 'For transportation to'
    Loading_on_board_despatch_taking_in_charge_at_from = (
        'Loading on board/despatch/taking in charge at/from'
    )
    Private_box = 'Private box'
    Next_port_of_discharge = 'Next port of discharge'
    Port_of_call = 'Port of call'
    Place_location_of_on_hire = 'Place/location of on-hire'
    Place_location_of_off_hire = 'Place/location of off-hire'
    Other_carriers_terminal = 'Other carriers terminal'
    Country_of_Value_Added_Tax__VAT__jurisdiction = (
        'Country of Value Added Tax (VAT) jurisdiction'
    )
    Contact_location = 'Contact location'
    Additional_internal_destination = 'Additional internal destination'
    Foreign_port_of_call = 'Foreign port of call'
    Maintenance_location = 'Maintenance location'
    Mutually_defined = 'Mutually defined'


class Type6(Enum):
    EdiCodeco = 'EdiCodeco'


class EdiCodeco(BaseModel):
    address: Optional[Address] = Field(None, description='The mailing address')
    alternateName: Optional[str] = Field(
        None, description='An alternative name for this item'
    )
    areaServed: Optional[str] = Field(
        None,
        description='The geographic area where a service or offered item is provided',
    )
    ata: Optional[AwareDatetime] = Field(
        None,
        description='Actual time of arrival or departure to/from Terminal. (ISO 8601 UTC format). See [UNTDID - D.95B - Segment DTM - C507 (2380)](https://service.unece.org/trade/untdid/d95b/uncl/uncl2380.htm)',
    )
    bookingCode: Optional[str] = Field(
        None,
        description='Booking Reference. See [UNTDID - D.95B - Segment RFF - C506 (1154)](https://service.unece.org/trade/untdid/d95b/uncl/uncl1154.htm)',
    )
    containerCarrierIdentification: Optional[str] = Field(
        None,
        description='Code identifying a party involved in a transaction. See [UNTDID - D.95B - Segment NAD - C082 (3039)](https://service.unece.org/trade/untdid/d95b/uncl/uncl3039.htm)',
    )
    containerClass: Optional[ContainerClass] = Field(
        None,
        description="Container class (indication of the action related to the equipment). Enum: 'Continental, Export, Import,Remain on board,Shifter,Transhipment'. See [UNTDID - D.95B - Segment EQD - 8249](https://service.unece.org/trade/untdid/d95b/uncl/uncl8249.htm)",
    )
    containerIdentification: Optional[str] = Field(
        None,
        description='Containter identification. See [UNTDID - D.95B - Segment EQD - C237 (8260)](https://service.unece.org/trade/untdid/d95b/uncl/uncl8260.htm)',
    )
    containerIsoCode: Optional[ContainerIsoCode] = Field(
        None,
        description="Coded description of the size and type of equipment. Enum 'Dime coated tank,Epoxy coated tank,IMO1,IMO2,IMO3,Pressurized tank,Refrigerated tank,Semi-refrigerated,Stainless steel tank,Nonworking reefer container 40 ft,Box pallet,Europallet,Scandinavian pallet,Trailer,Nonworking reefer container 20 ft,Exchangeable pallet,Semi-trailer,Tank container 20 ft.,Tank container 30 ft.,Tank container 40 ft.,Container IC 20 ft.,Container IC 30 ft.,Container IC 40 ft.,Refrigerator tank 20 ft.,Refrigerator tank 30 ft.,Refrigerator tank 40 ft.,Tank container IC 20 ft.,Tank container IC 30 ft.,Tank container IC 40 ft.,Refrigerator tank IC 20 ft.,Refrigerator tank IC 40 ft.,Movable case: L < 6,15m,Movable case: 6,15m < L < 7,82m,Movable case: 7,82m < L < 9,15m,Movable case: 9,15m < L < 10,90m,Movable case: 10,90m < L < 13,75m,Totebin,Temperature controlled container 20 ft,Temperature controlled container 40 ft'. See [UNTDID - D.95B - Segment EQD - C224 (8155)](https://service.unece.org/trade/untdid/d95b/uncl/uncl8155.htm)",
    )
    containerSeal: Optional[str] = Field(
        None,
        description='The number of a custom seal or another seal affixed to the containers. See [UNTDID - D.95B - Segment SEL - 9308](https://service.unece.org/trade/untdid/d95b/uncl/uncl9308.htm)',
    )
    containerWeight: Optional[float] = Field(
        None,
        description='Weight of the container. See [UNTDID - D.95B - Segment MEA - C174 (6314)](https://service.unece.org/trade/untdid/d95b/uncl/uncl6314.htm)',
    )
    dataProvider: Optional[str] = Field(
        None,
        description='A sequence of characters identifying the provider of the harmonised data entity',
    )
    dateCreated: Optional[AwareDatetime] = Field(
        None,
        description='Entity creation timestamp. This will usually be allocated by the storage platform',
    )
    dateModified: Optional[AwareDatetime] = Field(
        None,
        description='Timestamp of the last modification of the entity. This will usually be allocated by the storage platform',
    )
    description: Optional[str] = Field(None, description='A description of this item')
    destination: Optional[str] = Field(
        None,
        description='Final destination of the container (UN/LOCODE: United Nations Code for Trade and Transport Locations). See [UNTDID - D.95B - Segment LOC - C517 (3225)](https://service.unece.org/trade/untdid/d95b/uncl/uncl3225.htm) and [UN/LOCODE](https://unece.org/trade/cefact/unlocode-code-list-country-and-territory)',
    )
    destinationTransportType: Optional[str] = Field(
        None,
        description='Method of transport code (UN/ECE). See [UNTDID - D.95B - Segment TDT - C220 (8067)](https://service.unece.org/trade/untdid/d95b/uncl/uncl8067.htm) and [UN/ECE - Rec 19](https://unece.org/trade/uncefact/cl-recommendations)',
    )
    dischargingPort: Optional[str] = Field(
        None,
        description='Port where the container is discharged (UN/LOCODE: United Nations Code for Trade and Transport Locations). See [UNTDID - D.95B - Segment LOC - C517 (3225)](https://service.unece.org/trade/untdid/d95b/uncl/uncl3225.htm) and [UN/LOCODE](https://unece.org/trade/cefact/unlocode-code-list-country-and-territory)',
    )
    fileName: Optional[str] = Field(None, description='File name of EDI Codeco message')
    functionCode: Optional[FunctionCode] = Field(
        None,
        description="Code indicating the function of the message. Enum='Cancellation, Addition, Deletion, Change, Replace, Confirmation, Duplicate, Status, Original, Not found, Response, Not processed, Request, Advance notification, Reminder, Proposal, Cancel, to be reissued, Reissue, Seller initiated change, Replace heading section only, Replace item detail and summary only, Final transmission, Transaction on hold, Delivery instruction, Forecast, Delivery instruction and forecast, Not accepted, Accepted, with amendment in heading section, Accepted without amendment, Accepted, with amendment in detail section, Copy, Approval, Change in heading section, Accepted with amendment, Retransmission, Change in detail section, Reversal of a debit, Reversal of a credit, Reversal for cancellation, Request for deletion, Finishing/closing order, Confirmation via specific means, Additional transmission, Accepted without reserves, Accepted with reserves, Provisional, Definitive, Accepted, contents rejected, Settled dispute, Withdraw, Authorisation, Proposed amendment, Test'. See [UNTDID - D.95B - BGM - 1225](https://service.unece.org/trade/untdid/d95b/uncl/uncl1225.htm)",
    )
    id: Optional[
        Union[
            constr(
                pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!, :\\\\]+$',
                min_length=1,
                max_length=256,
            ),
            AnyUrl,
        ]
    ] = Field(None, description='Unique identifier of the entity')
    isContainerEmpty: Optional[bool] = Field(
        None,
        description='Information about if the container is full or empty. See [UNTDID - D.95B - Segment EQD - 8169](https://service.unece.org/trade/untdid/d95b/uncl/uncl8169.htm)',
    )
    loadingPort: Optional[str] = Field(
        None,
        description='Port where the container is loaded (UN/LOCODE: United Nations Code for Trade and Transport Locations). See [UNTDID - D.95B - Segment LOC - C517 (3225)](https://service.unece.org/trade/untdid/d95b/uncl/uncl3225.htm) and [UN/LOCODE](https://unece.org/trade/cefact/unlocode-code-list-country-and-territory)',
    )
    location: Optional[
        Union[Location, Location1, Location2, Location3, Location4, Location5]
    ] = Field(
        None,
        description='Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon',
    )
    messageRaw: Optional[str] = Field(None, description='Raw message of the EDI Codeco')
    messageVersion: Optional[str] = Field(
        None,
        description='Version of the message type. See [UNTDID - D.95B - UNH - S009 (0052)](https://service.unece.org/trade/untdid/d95b/trmd/codeco_d.htm#DSGI)',
    )
    name: Optional[str] = Field(None, description='The name of this item')
    operationType: Optional[OperationType] = Field(
        None,
        description="Code identifying the function of a location. Enum: 'Place of terms of delivery, Payment place, Goods receipt place, Place of departure, Place of delivery, Place of destination, Place/port of loading, Place of acceptance, Place/port of discharge, Port of discharge, Place of transhipment, Location of goods, Place of transfer responsibility, Place of transfer of ownership, Border crossing place, Warehouse, Factory/plant, Place of ultimate destination of goods, Terms of sale place, Customs office of clearance, Port of release, Port of entry, Country, City, Country of origin, Country of destination of goods, Railway station, Country of source, Building, Beginning of chargeable section, Baseport of discharge, Baseport of loading, Country of exportation/despatch, Country of ultimate destination, Country of last consignment, Country of first destination, Country of production, Country of trading, Customs office of entry, Customs office of exit, Place of Customs examination, Place of authentication of document, Customs office of destination (transit), Region of despatch, Region of destination, Region of production, Country of transit, Customs office of transit, Country of invalid transit guarantee, Country of destination (transit), Charge and freight due from, Manufacturing department, Charges and freight payable to, End of chargeable section, Place of payment, Full track loading or unloading, Place of arrival, Next port of call, On-carriage port, First optional place of discharge, Express railway station, Mixed cargo railway station, Second optional place of discharge, Next non-discharge port of call, Third optional place of discharge, Reconsolidation point, Fourth optional place of discharge, Bill of lading release office, Transhipment excluding this place, Transhipment limited to this place, Original port of loading, First port of call - non-discharging, First port of call - discharging, Place/port of first entry, Place of despatch, Fifth optional place of discharge, Pre-carriage port, Place of delivery (by on carriage), Transport contract place of acceptance, Transport contract place of destination, Country of valid transit guarantee, Place/port of conveyance initial arrival, Place of receipt, Place of registration, Place/location where special treatments have happened or must happen, Place of document issue, Routing, Station of application of additional costs, Place of lodgement of documents, Optional place of discharge, Place of empty equipment despatch, Place of empty equipment return, Place/port of warehouse entry, Country of first sale, Country of purchase, Place of transfer, Place of deconsolidation, Place of consumption, Region of origin, Place of consolidation, Rate combination point, Place of prolongation decision of delivery delay, Recharging place/location, Customs office of despatch, Country of despatch, Customs office of export, Free zone of export, Region of export/despatch, Customs office of departure, Customs office of transit guarantee, Country of transhipment, Country of sale, Customs office of destination, Wagon-load railway station, Siding, Last place/port of call of conveyance, Country of previous Customs procedure, Customs office of registration of previous Customs declaration, Participant sender location, Wage negotiation district, Place of ultimate destination of conveyance, Place of loading of empty equipment, Place of discharge of empty equipment, Region of delivery, Petroleum warehouse, Place of entry (Customs), Living animals care place, Re-icing place, Weighting place, Marshalling yard, Shopping station, Loading dock, Port connection, Place of expiry, Place of negotiation, Claims payable place, Documentary credit available in, Stowage cell, For transportation to, Loading on board/despatch/taking in charge at/from, Private box, Next port of discharge, Port of call, Place/location of on-hire, Place/location of off-hire, Other carriers terminal, Country of Value Added Tax (VAT) jurisdiction, Contact location, Additional internal destination, Foreign port of call, Maintenance location Mutually defined'. See [UNTDID - D.95B - Segment TDT - LOC - 3227](https://service.unece.org/trade/untdid/d95b/uncl/uncl3227.htm)",
    )
    originTransportType: Optional[str] = Field(
        None,
        description='Method of transport code (UN/ECE). See [UNTDID - D.95B - Segment TDT - C220 (8067)](https://service.unece.org/trade/untdid/d95b/uncl/uncl8067.htm) and [UN/ECE - Rec 19](https://unece.org/trade/uncefact/cl-recommendations)',
    )
    owner: Optional[
        List[
            Union[
                constr(
                    pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!,:\\\\]+$',
                    min_length=1,
                    max_length=256,
                ),
                AnyUrl,
            ]
        ]
    ] = Field(
        None,
        description='A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)',
    )
    receiverIdentification: Optional[str] = Field(
        None,
        description='Interchange Recipient Identification. See [UN/EDIFACT - S003](https://unece.org/trade/uncefact/unedifact/part-4-Annex-B)',
    )
    release: Optional[str] = Field(
        None,
        description='Release number within current version number. See [UNTDID - D.95B - UNH - S009 (0054)](https://service.unece.org/trade/untdid/d95b/trmd/codeco_d.htm#DSGI)',
    )
    seeAlso: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None, description='list of uri pointing to additional resources about the item'
    )
    senderIdentification: Optional[str] = Field(
        None,
        description='Interchange Sender Identification. See [UN/EDIFACT - S002](https://unece.org/trade/uncefact/unedifact/part-4-Annex-B)',
    )
    sentAt: Optional[AwareDatetime] = Field(
        None,
        description='Date and time of message has been sent represented by an ISO 8601 UTC format. See [UN/EDIFACT - S004](https://unece.org/trade/uncefact/unedifact/part-4-Annex-B)',
    )
    source: Optional[str] = Field(
        None,
        description='A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object',
    )
    travelReference: Optional[str] = Field(
        None,
        description='Conveyance reference number. See [UNTDID - D.95B - Segment TDT - 8028](https://service.unece.org/trade/untdid/d95b/uncl/uncl8028.htm)',
    )
    truckLicenseCode: Optional[str] = Field(
        None,
        description='License Plate of the Truck. See [UNTDID - D.95B - Segment TDT - C222 (8213)](https://service.unece.org/trade/untdid/d95b/uncl/uncl8213.htm)',
    )
    type: Optional[Type6] = Field(
        None, description='NGSI Entity type. It has to be EdiCodeco'
    )
    vesselCallSign: Optional[str] = Field(
        None,
        description='Maritime call signs are call signs assigned as unique identifiers to vessels. See [UNTDID - D.95B - Segment TDT - C222 (8213)](https://service.unece.org/trade/untdid/d95b/uncl/uncl8213.htm)',
    )
    vesselCarrier: Optional[str] = Field(
        None,
        description='Vessel carrier Identification (identification of party undertaking or arranging transport of goods between named points). See [UNTDID - D.95B - Segment TDT - C040 (3127)](https://service.unece.org/trade/untdid/d95b/uncl/uncl3127.htm)',
    )
    vesselImo: Optional[float] = Field(
        None,
        description='International Maritime Organization Number (a global forever UID). See [UNTDID - D.95B - Segment TDT - C222 (8213)](https://service.unece.org/trade/untdid/d95b/uncl/uncl8213.htm)',
    )
    vesselMmsi: Optional[float] = Field(
        None,
        description="Marine Mobile Service Identity Number (a temporarily assigned UID, issued by that object's current flag state). See [UNTDID - D.95B - Segment TDT - C222 (8213)](https://service.unece.org/trade/untdid/d95b/uncl/uncl8213.htm)",
    )
    vesselName: Optional[str] = Field(
        None,
        description='Vessel Name. See [UNTDID - D.95B - Segment TDT - C222 (8212)](https://service.unece.org/trade/untdid/d95b/uncl/uncl8212.htm)',
    )
    vesselVoyage: Optional[str] = Field(
        None,
        description='Reference number of vessel voyage. See [UNTDID - D.95B - Segment RFF - C506 (1154)](https://service.unece.org/trade/untdid/d95b/uncl/uncl1154.htm)',
    )
