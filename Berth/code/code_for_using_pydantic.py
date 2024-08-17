from __future__ import annotations

from enum import Enum
from typing import List, Optional, Union

from pydantic import AnyUrl, AwareDatetime, BaseModel, Field, RootModel, constr


class ActivityCode(Enum):
    ZGR = 'ZGR'
    ZPV = 'ZPV'
    ZCA = 'ZCA'
    ZRA = 'ZRA'
    ZRF = 'ZRF'
    ZRT = 'ZRT'
    ZDA = 'ZDA'
    ZTA = 'ZTA'
    ZTF = 'ZTF'
    ZVO = 'ZVO'
    ZAF = 'ZAF'
    ZIN = 'ZIN'
    ZIP = 'ZIP'
    ZAR = 'ZAR'
    ZAO = 'ZAO'
    ZAB = 'ZAB'
    ZOP = 'ZOP'
    ZCT = 'ZCT'
    ZTI = 'ZTI'
    ZBO = 'ZBO'
    ZCO = 'ZCO'
    ZRE = 'ZRE'
    ZDE = 'ZDE'
    ZAP = 'ZAP'
    ZDR = 'ZDR'
    ZPB = 'ZPB'
    ZCL = 'ZCL'
    ZDJ = 'ZDJ'
    ZMR = 'ZMR'
    ZPR = 'ZPR'
    ZRM = 'ZRM'
    ZVA = 'ZVA'
    ZDS = 'ZDS'
    ZOT = 'ZOT'
    EST = 'EST'
    ZSA = 'ZSA'
    ZSH = 'ZSH'
    ZSE = 'ZSE'
    ZSC = 'ZSC'
    ZSV = 'ZSV'


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


class BerthingTypeCode(Enum):
    ABV = 'ABV'
    ABX = 'ABX'
    AB1 = 'AB1'
    AB2 = 'AB2'
    AEX = 'AEX'
    AX1 = 'AX1'
    AEV = 'AEV'
    REM = 'REM'
    REX = 'REX'
    RE1 = 'RE1'
    RE2 = 'RE2'
    RPM = 'RPM'
    RPV = 'RPV'
    RPX = 'RPX'
    RXM = 'RXM'
    RXV = 'RXV'
    RXX = 'RXX'
    RX1 = 'RX1'
    AE1 = 'AE1'
    AE2 = 'AE2'
    APM = 'APM'
    APV = 'APV'
    APX = 'APX'
    AXM = 'AXM'
    AXV = 'AXV'
    AXX = 'AXX'
    AX2 = 'AX2'
    FBM = 'FBM'
    FBV = 'FBV'
    FBX = 'FBX'
    FB1 = 'FB1'
    FB2 = 'FB2'
    FEM = 'FEM'
    FEV = 'FEV'
    FEX = 'FEX'
    FE1 = 'FE1'
    FE2 = 'FE2'
    FPM = 'FPM'
    FPV = 'FPV'
    FPX = 'FPX'
    FP1 = 'FP1'
    FP2 = 'FP2'
    FXM = 'FXM'
    FXV = 'FXV'
    FX1 = 'FX1'
    FX2 = 'FX2'
    RBM = 'RBM'
    RBX = 'RBX'
    RB1 = 'RB1'
    RB2 = 'RB2'
    RX2 = 'RX2'
    YBM = 'YBM'
    YBV = 'YBV'
    YBX = 'YBX'
    YB1 = 'YB1'
    YB2 = 'YB2'
    YEM = 'YEM'
    YEV = 'YEV'
    YEX = 'YEX'
    YE1 = 'YE1'
    YE2 = 'YE2'
    YPM = 'YPM'
    YPV = 'YPV'
    YPX = 'YPX'
    YP1 = 'YP1'
    YP2 = 'YP2'
    YXM = 'YXM'
    YXV = 'YXV'
    YX1 = 'YX1'
    YX2 = 'YX2'
    ABM = 'ABM'
    AEM = 'AEM'
    FXX = 'FXX'
    YXX = 'YXX'
    AP1 = 'AP1'
    AP2 = 'AP2'
    RBV = 'RBV'
    REV = 'REV'


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
    INITIATED = 'INITIATED'
    REQUESTED = 'REQUESTED'
    REJECTED = 'REJECTED'
    INVOICING = 'INVOICING'
    INVOICED = 'INVOICED'


class Type6(Enum):
    Berth = 'Berth'


class Berth(BaseModel):
    activityCode: Optional[ActivityCode] = Field(
        None,
        description='Activity during the stop in berth. It can be cargo operations or a number of activities related to the ship-port activities. Enum: ZGR=Major repair; ZPV=Provisioning; ZCA=Shipyard Construction; ZRA=Major shipyard repair; ZRF=Repair afloat with crew personnel; ZRT=Repair at anchor with personnel other than the crew; ZDA=Shipyard scrapping; ZTA=Shipyard Transformation; ZTF=Transformation; ZVO=Official visit; ZAF=Forced arrival; ZIN=Inactive; ZIP=Fishing inactivity; ZAR=Provisioning at docking; ZAO=Provisioning at anchor; ZAB=Provisioning at docking by barge; ZOP=Port operations of commercial traffic; ZCT=Sightseeing cruises; ZTI=Internal traffic; ZBO=Launching; ZCO=Construction; ZRE=Vessel intended for towing service; ZDE=Scrapyard; ZAP=Fishing and artisanal vessels in loading and unloading operations of fresh fish; ZDR=Vessel intended for dredging; ZPB=Biological stoppage; ZCL=No license; ZDJ=Judicial deposit; ZMR=Vessel intended for mooring service; ZPR=Vessel intended for pilotage service; ZRM=Trailer; ZVA=Access to slipway; ZDS=Vessel in dry dock; ZOT=Other; EST=Stay; ZSA=Water Supply; ZSH=Ice Supply; ZSE=Electrical Energy Supply; ZSC=Fuel Supply; ZSV=Victualling;',
    )
    address: Optional[Address] = Field(None, description='The mailing address')
    agentLegalCode: Optional[str] = Field(
        None, description="Legal identifier code of the PortCall's ship Agent"
    )
    agentName: Optional[str] = Field(None, description="Name of PortCall's ship Agent")
    alternateName: Optional[str] = Field(
        None, description='An alternative name for this item'
    )
    areaServed: Optional[str] = Field(
        None,
        description='The geographic area where a service or offered item is provided',
    )
    arrivalDraught: Optional[float] = Field(
        None, description='Draught at first-line secured for arriving navigation'
    )
    ataBerth: Optional[AwareDatetime] = Field(
        None,
        description='Represented by an ISO 8601 UTC format, Actual time of arrival to Berth',
    )
    atdBerth: Optional[AwareDatetime] = Field(
        None,
        description='Represented by an ISO 8601 UTC format. Actual time of departure from Berth',
    )
    authorizationRemarks: Optional[str] = Field(
        None, description='Conditions to the berthing written by Port Authority'
    )
    authorizedAt: Optional[AwareDatetime] = Field(
        None,
        description='Represented by an ISO 8601 UTC format, Date and time of authorization by port Authority and Maritime Authority. ',
    )
    berthCode: Optional[str] = Field(
        None,
        description='Code identifying the port-facility for this stop of the vessel. Format: <oid>:berth:99999',
    )
    berthName: Optional[str] = Field(
        None, description='Name of the port-facility for this stop of the vessel'
    )
    berthingTypeCode: Optional[BerthingTypeCode] = Field(
        None,
        description='Codes for identifying the Type of berthing/mooring in the interface ship-port. Enum: ABV=Board port to ship; ABX=Port berthed; AB1=Bouched port by bow; AB2=Bouched port by stern; AEX=Starboard docked; AX1=Docked by bow; AEV=Board starboard to ship; REM=Boarded starboard at the pier; REX=Starboard bow; RE1=Starboard bow by bow; RE2=Cracked starboard by stern; RPM=Toe-to-spring twisting; RPV=Boarded from tip to ship; RPX=Ringed point; RXM=To moor alongside a dock; RXV=Moored to another vessel; RXX=Moored ; RX1=Tangled by bow; AE1=Bouched starboard by bow; AE2=Bouched starboard by stern; APM=Pocketed to the pier; APV=Pocket to ship; APX=Point docking; AXM=docked at the pier; AXV=Boarded to ship; AXX=docked; AX2=Docked by stern; FBM=Anchored port side at the pier; FBV=Anchored port side to ship; FBX=Port anchored; FB1=Anchored port by bow; FB2=Anchored port by stern; FEM=Anchored starboard to the pier; FEV=Anchored starboard to ship; FEX=Anchored starboard; FE1=Anchored starboard by bow; FE2=Anchored starboard by stern; FPM=Toe-to-pier mooring; FPV=Anchoring tip to ship; FPX=Point anchoring; FP1=Anchoring tip by bow; FP2=Anchoring tip by stern; FXM=Anchored at the pier; FXV=Anchored to ship; FX1=Anchored by bow; FX2=Anchored by stern; RBM=Moored portside to the dock; RBX=Battered port side; RB1=Bulked port by bow; RB2=Bulked on port side by stern; RX2=Tangled by stern; YBM=Tethered to the port buoy at the pier; YBV=Tethered to the buoy on the port side of the ship; YBX=Tethered to port buoy; YB1=Tied to port buoy by bow; YB2=Tied to port buoy by stern; YEM=Tethered to the starboard buoy at the pier; YEV=Tethered to the starboard buoy of the ship; YEX=Tethered to starboard buoy; YE1=Tied to starboard buoy by bow; YE2=Tied to starboard buoy by stern; YPM=Tethered to the end buoy at the pier; YPV=Tethered to the buoy end-to-ship; YPX=Tied to tip buoy; YP1=Tethered to tip buoy by bow; YP2=Tied to the tip buoy by stern; YXM=Tethered to the buoy at the pier; YXV=Tethered to the buoy to the ship; YX1=Tethered to buoy by bow; YX2=Tethered to buoy by stern; ABM=Port berthed to the pier; AEM=Moored starboard to dock; FXX=Anchoring; YXX=Tethered to buoy without further indication; AP1=Boarding tip by bow; AP2=Pocketed fore and aft; RBV=Bulked port to ship; REV=Wheeled starboard to ship;. ',
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
    departureDraught: Optional[float] = Field(
        None, description='Draught at last-line released for departure navigation'
    )
    description: Optional[str] = Field(None, description='A description of this item')
    etaBerth: Optional[AwareDatetime] = Field(
        None,
        description='Represented by an ISO 8601 UTC format, Date and time of Estimated Time of Arrival to Berth expected by Port Authority (ISO 8601 UTC format). [EMSWe: DE-005-09] [EDI: DTM-2005-132] [S211: locationState.timeType.ESTIMATED] [IMO: IMO0064]',
    )
    etdBerth: Optional[AwareDatetime] = Field(
        None,
        description='Represented by an ISO 8601 UTC format, Date and time of Estimated Time of Departure from Berth, expected by Port Authority. [EMSWe: DE-005-04] [EDI: DTM-2005-133] [S211: locationState.timeType.ESTIMATED] [IMO: IMO0066]',
    )
    firstBollard: Optional[str] = Field(
        None, description='First bollard identifier in port facility'
    )
    gln: Optional[float] = Field(
        None,
        description="ISO/IEC 6523:'https://schema.org/Number'. Optional code of the location. The Global Location Number (GLN) is a 13 digits-unique number that is assigned to locations to enable them to be identified uniquely worldwide, allocated to any location in the supply chain. These GLNs can be used to identify any legal, physical and functional locations",
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
    lastBollard: Optional[str] = Field(
        None, description='Last bollard identifier in port facility'
    )
    location: Optional[
        Union[Location, Location1, Location2, Location3, Location4, Location5]
    ] = Field(
        None,
        description='Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon',
    )
    mooringLines: Optional[float] = Field(None, description='Number of mooring lines. ')
    mrn: Optional[str] = Field(
        None,
        description="MRN coded identifier. It has to be related to the entity in a way that is well-known by different organisms the meaning and the initiator of the entity, and all next parties will maintain on its original value. This identifier must be an UNIQUE identifier of the PortCall entity assigned by the system who created on first the entity. This URN should Conforms MRN & IETF specifically RFC 2141, RFC 5234, and RFC 8141. The proposed format is id::='urn:mrn:<OID>:<ONSS>:portcalls:berth:id:[0-9]+' where OID:= Organisation UN/LOCODE, OONSS:=Organization Name of Service, 9999999 an increasing, unique identifier that the issuer of the Berth entity will identify on his systems (i.e. a SQL row-id), i.e. urn:mrn:eshuv:portcalls:berth:id:2024012. See [Unlocode](https://unece.org/trade/cefact/unlocode-code-list-country-and-territory). In international standards is also known as [Ship's Visit]",
    )
    name: Optional[str] = Field(None, description='The name of this item')
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
    portCallNumber: Optional[str] = Field(None, description='PortCall identifier')
    portCallRef: Optional[
        Union[
            constr(
                pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!, :\\\\]+$',
                min_length=1,
                max_length=256,
            ),
            AnyUrl,
        ]
    ] = Field(None, description='Relationship.Reference to parent PortCall entity. ')
    portCode: Optional[str] = Field(None, description='Code of the port of the call')
    ptaBerth: Optional[AwareDatetime] = Field(
        None,
        description='Represented by an ISO 8601 UTC format, Planned time of arrival to Berth',
    )
    ptdBerth: Optional[AwareDatetime] = Field(
        None,
        description='Represented by an ISO 8601 UTC format. Planned time of departure from Berth',
    )
    remarks: Optional[str] = Field(
        None, description='Remarks of the berthing, by Agent at Port or others'
    )
    requestedAt: Optional[AwareDatetime] = Field(
        None,
        description='Represented by an ISO 8601 UTC format, Date and time of the berthing request by the ship agent. ',
    )
    rtaBerth: Optional[AwareDatetime] = Field(
        None,
        description='Represented by an ISO 8601 UTC format, Date and time of Requested Time of Arrival by ship-agent (ISO 8601 UTC format).. [EMSWe: DE-005-09] [EDI: DTM-2005-132] [S211: locationState.timeType.ESTIMATED] [IMO: IMO0064]',
    )
    rtdBerth: Optional[AwareDatetime] = Field(
        None,
        description='Represented by an ISO 8601 UTC format, Date and time of Requested Time of Departure by ship-agent (ISO 8601 UTC format). [EMSWe: DE-005-09] [EDI: DTM-2005-132] [S211: locationState.timeType.ESTIMATED] [IMO: IMO0064]',
    )
    seeAlso: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None, description='list of uri pointing to additional resources about the item'
    )
    source: Optional[str] = Field(
        None,
        description='A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object',
    )
    status: Optional[Status] = Field(
        None,
        description="Current status of the Berthing in its lifetime, from request to authorization and completion. Enum:'ACCEPTED, AUTHORIZED, CANCELLED, COMPLETED, DENIED, INITIATED, REQUESTED, REJECTED, INVOICING, INVOICED'. [EMSWe: DE-019-07] [EDI: BGM-1225] [S211: serviceState: timeSequence:VESSEL] ",
    )
    stopRank: Optional[float] = Field(
        None,
        description='Rank or Number of this stop in the PortCall activity ordered by arrival time in the sequence of stops (berthing/anchor area)',
    )
    terminal: Optional[str] = Field(None, description='Common name of the Terminal')
    type: Optional[Type6] = Field(
        None, description='NGSI Entity type. It has to be Berth'
    )
    year: Optional[float] = Field(None, description='Year of the init of the berthing')
