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


class AuthorizedBy(Enum):
    PORT_AUTHORITY = 'PORT_AUTHORITY'
    ARMY_AUTHORITY = 'ARMY_AUTHORITY'
    PORT_ARMY_AUTHORITIES = 'PORT_ARMY_AUTHORITIES'


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


class Status(Enum):
    ACCEPTED = 'ACCEPTED'
    AUTHORIZED = 'AUTHORIZED'
    CANCELLED = 'CANCELLED'
    COMPLETED = 'COMPLETED'
    DENIED = 'DENIED'
    ESTIMATED = 'ESTIMATED'
    INITIATED = 'INITIATED'
    REQUESTED = 'REQUESTED'
    REJECTED = 'REJECTED'
    INVOICING = 'INVOICING'
    INVOICED = 'INVOICED'
    OPERATIONAL = 'OPERATIONAL'


class Type6(Enum):
    PortCall = 'PortCall'


class ShipTypeCategory(Enum):
    CONTAINER = 'CONTAINER'
    GENERAL_CARGO_NON_SPECIALIZED = 'GENERAL CARGO NON SPECIALIZED'
    LIQUID_BULK = 'LIQUID BULK'
    DRY_BULK = 'DRY BULK'
    CRUISE = 'CRUISE'


class ShipTypeClass(Enum):
    MULTI_DECKER = 'MULTI-DECKER'
    CHEMICAL_TANKER = 'CHEMICAL TANKER'
    FULL_CONTAINER = 'FULL CONTAINER'
    OIL_TANKER = 'OIL TANKER'
    BULK_CARRIER = 'BULK CARRIER'
    LG_TANKER = 'LG TANKER'


class Vessel(BaseModel):
    imo: Optional[float] = Field(
        None,
        description='IMO ship identification number, following the [scheme](https://www.imo.org/en/OurWork/IIIS/Pages/IMO-Identification-Number-Schemes.aspx) defined by the International Maritime Organization. [EMSWe: DE-003-03] [EDIFACT:TDT-8213] [IALA_S211:vesselId] [IMO:IMO0140]. To be deprecated in this object',
    )
    shipName: Optional[str] = Field(
        None, description='Name of the vessel. To To be deprecated in this object'
    )
    shipTypeCategory: Optional[ShipTypeCategory] = Field(
        None,
        description="Description of vessel category. Enum: 'CONTAINER, GENERAL CARGO NON SPECIALIZED, LIQUID BULK, DRY BULK, CRUISE'. To be deprecated in this object",
    )
    shipTypeClass: Optional[ShipTypeClass] = Field(
        None,
        description="Description of vessel class. Enum: 'MULTI-DECKER, CHEMICAL TANKER, FULL CONTAINER, OIL TANKER, BULK CARRIER, LG TANKER'. To be deprecated in this object",
    )


class VesselTypeCategory(Enum):
    CONTAINER = 'CONTAINER'
    GENERAL_CARGO_NON_SPECIALIZED = 'GENERAL CARGO NON SPECIALIZED'
    LIQUID_BULK = 'LIQUID BULK'
    DRY_BULK = 'DRY BULK'
    CRUISE = 'CRUISE'


class VesselTypeClass(Enum):
    MULTI_DECKER = 'MULTI-DECKER'
    CHEMICAL_TANKER = 'CHEMICAL TANKER'
    FULL_CONTAINER = 'FULL CONTAINER'
    OIL_TANKER = 'OIL TANKER'
    BULK_CARRIER = 'BULK CARRIER'
    LG_TANKER = 'LG TANKER'


class PortCall(BaseModel):
    UNLOCODE: Optional[str] = Field(
        None,
        description='United Nations Code for Trade and Transport Locations, [UN/LOCODE](https://unece.org/trade/cefact/unlocode-code-list-country-and-territory), of the port. to be deprecated. Use portCode instead',
    )
    address: Optional[Address] = Field(None, description='The mailing address')
    agentChangeDate: Optional[AwareDatetime] = Field(
        None, description='[EMSWe: -] [EDI: -] [S211: -] [IMO: -] '
    )
    agentLegalCode: Optional[str] = Field(
        None,
        description="Legal identifier code of the PortCall's ship Agent. [EMSWe: -] [EDI: -] [S211: -] [IMO: -] ",
    )
    agentName: Optional[str] = Field(
        None,
        description='The name of the Agent at Port of the ship (aka consignor). [EMSWe: DE-009-01] [EDI: NAD-3035-ZME-CV] [IMO: IMO0002]',
    )
    alternateName: Optional[str] = Field(
        None, description='An alternative name for this item'
    )
    areaServed: Optional[str] = Field(
        None,
        description='The geographic area where a service or offered item is provided',
    )
    arrivalDate: Optional[AwareDatetime] = Field(
        None,
        description='Date/time of ship arrival at port area. To be deprecated. Use ata instead',
    )
    arrivalDateScheduled: Optional[AwareDatetime] = Field(
        None,
        description='Scheduled date/time of ship arrival at port area, as declared by shipping agent. To be deprecated. Use eta instead',
    )
    ata: Optional[AwareDatetime] = Field(
        None,
        description='Date and time of Actual Time of Arrival to Port (ISO 8601 UTC format). [EMSWe: DE-005-02] [IALA_S211:locationState.timeType.ACTUAL] [IMO:IMO0063]',
    )
    atd: Optional[AwareDatetime] = Field(
        None,
        description='Date and time of Actual Time of Departure  from Port.  (ISO 8601 UTC format). [IALA_S211:timeType=2] [EMSWe: DE-005-03] [IALA_S211:locationState.timeType.ACTUAL] [IMO:IMO0065] ',
    )
    authorizationDate: Optional[AwareDatetime] = Field(
        None,
        description='Date and time of authorization represented by an ISO 8601 UTC format',
    )
    authorizedBy: Optional[AuthorizedBy] = Field(
        None,
        description='Codes to identify which authority has approved or denied the visit of the ship. [EMSWe: DE-027-01] [EDIFACT:BGM-4443] [IMO:IMO0010]',
    )
    callSign: Optional[str] = Field(
        None,
        description='Identification signal of a vessel when initially connecting by radio [EMSWe: DE-065-05] [EDI: BGM-RFF] [S211: Call Name / Call Sign] [IMO: IMO0136] ',
    )
    crewArrival: Optional[float] = Field(
        None,
        description='Number of crew at arrival. [EMSWe: DE-013-03] [EDIFACT:QTY-6063-ZTE] [IMO:IMO0086]',
    )
    crewDeparture: Optional[float] = Field(
        None,
        description='Number of crew at departure. [EMSWe: DE-013-03] [EDIFACT:QTY-6063-ZTS] [IMO:IMO0086] ',
    )
    dangerousGoodsCarried: Optional[bool] = Field(
        None,
        description="A 'yes/no' indicator whether the ship is carrying any dangerous goods.[EMSWe: DE-018-02] [EDIFACT:FTX-4441-ZCD] [IMO:IMO0046]",
    )
    dangerousGoodsLoading: Optional[bool] = Field(
        None,
        description="A 'yes/no' indicator whether the ship is loading any dangerous goods in this port. [EMSWe: DE-018-02] [EDIFACT:FTX-4441-ZDD] [IMO:IMO0046]",
    )
    dangerousGoodsUnloading: Optional[bool] = Field(
        None,
        description="A 'yes/no' indicator whether the ship is unloading any dangerous goods in this port. [EMSWe: DE-018-02] [EDIFACT:FTX-4441-ZBD] [IMO:IMO0046]",
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
    departureAuthorizationDate: Optional[AwareDatetime] = Field(
        None,
        description='Date and time of authorization for the departure by authorities represented by an ISO 8601 UTC format',
    )
    departureDate: Optional[AwareDatetime] = Field(
        None,
        description='Date/time of ship leaving port area. To be deprecated. Use atd instead',
    )
    departureDateScheduled: Optional[AwareDatetime] = Field(
        None,
        description='Scheduled date/time of ship leaving port area, as declared by shipping agent. To be deprecated. Use etd instead',
    )
    description: Optional[str] = Field(None, description='A description of this item')
    eta: Optional[AwareDatetime] = Field(
        None,
        description='Date and time of Estimated Time of Arrival to Port expected by Port Authority  (ISO 8601 UTC format). [EMSWe: DE-005-09] [EDIFACT:DTM-2005-132] [IALA_S211:locationState.timeType.ESTIMATED] [IMO:IMO0064]',
    )
    etd: Optional[AwareDatetime] = Field(
        None,
        description='Date and time of Estimated Time of Departure  from Port, expected by Port Authority  (ISO 8601 UTC format). [EMSWe: DE-005-04] [EDIFACT:DTM-2005-133] [IALA_S211:locationState.timeType.ESTIMATED] [IMO:IMO0066]',
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
    imo: Optional[float] = Field(
        None,
        description='IMO ship identification number, following the [scheme](https://www.imo.org/en/OurWork/IIIS/Pages/IMO-Identification-Number-Schemes.aspx) defined by the International Maritime Organization. [EMSWe: DE-003-03] [EDIFACT:TDT-8213] [IALA_S211:vesselId] [IMO:IMO0140]',
    )
    interiorTraffic: Optional[bool] = Field(None, description='')
    lastPortCode: Optional[str] = Field(
        None,
        description='Last port of call, coded.The code representing the port immediately previous to the port of arrival, if available. [EMSWe: DE-005-05] [EDIFACT:LOC-3227-92] [IMO:IMO0076] ',
    )
    location: Optional[
        Union[Location, Location1, Location2, Location3, Location4, Location5]
    ] = Field(
        None,
        description='Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon',
    )
    manifestActivated: Optional[bool] = Field(None, description='')
    manifestActivationDate: Optional[AwareDatetime] = Field(
        None,
        description='Date and time of approval of the cargo manifest. [MSWE: DE-036-04:Manifest number]',
    )
    masterName: Optional[str] = Field(
        None,
        description='Name of master [EMSWe: DE-053-01] [EDIFACT:NAD-3035-ZME] [IMO:IMO0083]',
    )
    mmsi: Optional[float] = Field(
        None,
        description="Marine Mobile Service Identity Number (a temporarily assigned UID, issued by that object's current flag state)[EMSWe: DE-068-09] [EDIFACT:TDT-1131] [IALA_S211:vesselId] [IMO:IMO0178]",
    )
    mrn: Optional[str] = Field(
        None,
        description="MRN coded identifier. It has to be related to the entity in a way that is well-known by different organisms the meaning and the initiator of the entity, and all next parties will maintain on its original value. This identifier must be an UNIQUE identifier of the PortCall entity assigned by the system who created on first the entity. This URN should Conforms MRN & IETF specifically RFC 2141, RFC 5234, and RFC 8141. The proposed format is id::='urn:mrn:<OID>:<ONSS>:portcalls:portcall:id:[0-9]+' where OID:= Organisation UN/LOCODE, OONSS:=Organization Name of Service, 9999999 an increasing, unique identifier that the issuer of the PortCall entity will identify on his systems (i.e. a SQL row-id), i.e. urn:mrn:eshuv:portcalls:portcall:id:19002. See [Unlocode](https://unece.org/trade/cefact/unlocode-code-list-country-and-territory)In international standards is also known as [Ship's Visit]",
    )
    name: Optional[str] = Field(None, description='The name of this item')
    nextPortCode: Optional[str] = Field(
        None,
        description='Next port of call, coded.The code representing the port immediately previous to the port of arrival, if available.. Related to IALA_S211:nestPortCallCod / IMO. [EMSWe: DE-005-07] [EDIFACT:LOC-3227-61] [IMO:IMO0120]',
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
    passengersArrival: Optional[float] = Field(
        None,
        description='Number of passengers at arrival. [EMSWe: DE-013-02] [EDIFACT:QTY-6063-ZPE] [IMO:IMO0087].',
    )
    passengersDeparture: Optional[float] = Field(
        None,
        description='Number of passengers at departure. [EMSWe: DE-013-02] [EDIFACT:QTY-6063-ZPS] [IMO:IMO0087]',
    )
    portCallNumber: Optional[str] = Field(
        None,
        description='Port call identifier in MRN format. First element of the NSS should be the 5 character UN/Locode of the port, later the YEAR and finishing with a sequential number in this port [LLLLLYYYY99999] where LLLLL is the UN/LOCODE of the visited port, YYYY is the year, and 99999 is a unique sequential number assigned by port authority unique on each year (i.e. ESHUV202310323). An abbreviation can be used for UN/LOCODE (i.e. H202310323).  The portCallNumber is assigned during the initial steps of the visit, but could be null at the beginning. In international standards is also known as [Port Call ID], [Visit ID] or [Port Call Coded]. See [Unlocode](https://unece.org/trade/cefact/unlocode-code-list-country-and-territory) [EMSWe: DG-004/DG-004-01] [EDIFACT:BGM-1004] [IALA_S211:portCallId] [IMO:IMO108+IMO0153]',
    )
    portCode: Optional[str] = Field(
        None,
        description='United Nations Code for Trade and Transport Locations. See [Unlocode](https://unece.org/trade/cefact/unlocode-code-list-country-and-territory) [EMSWe: DE-004-04] [EDIFACT:LOC-3227-153] [IALA_S211:portCode] [IMO:IMO0108]',
    )
    pta: Optional[AwareDatetime] = Field(
        None,
        description='Date and time of Planned Time of Arrival to Port by Port Authority Berthing Plan  (ISO 8601 UTC format). [EDIFACT:DTM-2005-155] [IALA_S211:locationState.timeType.PLANNED] [IMO:IMO0235]',
    )
    ptd: Optional[AwareDatetime] = Field(
        None,
        description='Date and time of Planned Time of Departure  from Port, planned by Port Authority Berthing Plan  (ISO 8601 UTC format). [EDI: DTM-2005-156] [S211: locationState.timeType.PLANNED] [IMO: IMO0236]',
    )
    regularLine: Optional[str] = Field(
        None,
        description='Name of the regular line if any. [EMSWe: DE-004-02] [EDIFACT:-] [IMO:-]',
    )
    remarks: Optional[str] = Field(
        None,
        description='Comments about this PortCall by the Porth Authority. [EMSWe: DE-038-01] [EDIFACT:FTX-4440-AAI] [IALA_S211:comment] [IMO: IMO0196]',
    )
    rta: Optional[AwareDatetime] = Field(
        None,
        description='Date and time of Requested Time of Arrival to Port. Requested by Consignee to Port Authority  (ISO 8601 UTC format). [EDIFACT:DTM-2005-178] [IALA_S211:locationState.timeType.REQUIRED] [IMO:IMO0234]',
    )
    rtd: Optional[AwareDatetime] = Field(
        None,
        description='Date and time of Requested Time of Departure from Port. Requested by Consignee to Port Authority  (ISO 8601 UTC format). [EDIFACT:DTM-2005-189] [IALA_S211:locationState.timeType.REQUIRED] [IMO:IMO0237]',
    )
    secondAgentLegalCode: Optional[str] = Field(
        None,
        description="Legal identifier code of the PortCall's ship Agent. [EMSWe: -] [EDI: -] [S211: -] [IMO: -] ",
    )
    secondAgentName: Optional[str] = Field(
        None,
        description='The name of the new Agent at Port of the Sipping Line and usually the consignor or the load. [EMSWe: DE-009-01] [EDI: NAD-3035-ZME-CV] [IMO: IMO0002] ',
    )
    seeAlso: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None, description='list of uri pointing to additional resources about the item'
    )
    shipName: Optional[str] = Field(None, description='Name of the vessel')
    source: Optional[str] = Field(
        None,
        description='A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object',
    )
    status: Optional[Status] = Field(
        None,
        description="Current status of the PortCall in its lifetime, from request to authorization by port and civil authorities and completion. [EMSWe: DE-019-07] [EDIFACT:BGM-1225] [IALA_S211:serviceState: timeSequence:VESSEL]. Enum:'ACCEPTED, AUTHORIZED, CANCELLED, COMPLETED, DENIED, ESTIMATED, INITIATED, REQUESTED, REJECTED, INVOICING, INVOICED, OPERATIONAL'",
    )
    terminal: Optional[str] = Field(
        None, description='Name of the terminal [EMSWe:-] [EDIFACT:-] [IMO:-]'
    )
    type: Optional[Type6] = Field(
        None, description='NGSI Entity type. It has to be PortCall'
    )
    vessel: Optional[Vessel] = Field(
        None,
        description='Calling vessel of the portcall. To be deprecated. Use individual attributes IMO, vesselTypeCategory, vesselTypeCategory, vesselName. To be deprecated in this object',
    )
    vesselAgent: Optional[str] = Field(
        None,
        description='Vessel Agent of the portcall. To be deprecated. Use agentName instead',
    )
    vesselName: Optional[str] = Field(
        None,
        description='Name of the Vessel. [EMSWe: DE-003-07] [EDIFACT:TDT-8212] [IMO:IMO0142]',
    )
    vesselRef: Optional[
        Union[
            constr(
                pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!, :\\\\]+$',
                min_length=1,
                max_length=256,
            ),
            AnyUrl,
        ]
    ] = Field(
        None,
        description='Related PortCallVessel with all fields loaded with further info. Reference to MarineTransport.MasterVessel/schema.json',
    )
    vesselTypeCategory: Optional[VesselTypeCategory] = Field(
        None,
        description="Description of vessel category. Enum: 'CONTAINER, GENERAL CARGO NON SPECIALIZED, LIQUID BULK, DRY BULK, CRUISE'",
    )
    vesselTypeClass: Optional[VesselTypeClass] = Field(
        None,
        description="Description of vessel class. Enum: 'MULTI-DECKER, CHEMICAL TANKER, FULL CONTAINER, OIL TANKER, BULK CARRIER, LG TANKER'",
    )
    voyageCode: Optional[str] = Field(
        None,
        description='Voyage code (unique ID of a voyage). To be deprecated. Use voyageNumber instead',
    )
    voyageNumber: Optional[str] = Field(
        None, description='Number of voyage. [EMSWe: DE-004-02] [EDIFACT:-] [IMO:-]'
    )
    wasteAgreementExists: Optional[bool] = Field(
        None,
        description='All waste delivery indicator. Waste collection paid indicator. Exists agreement with Port Authority for waste discharge and treatment. [EDIFACT:FTX-4441-ZRS/ZRL] [IALA_S211:locationReferenceObject. SLUDGE_VESSEL]',
    )
