from __future__ import annotations

from enum import Enum
from typing import List, Optional, Union

from pydantic import (
    AnyUrl,
    AwareDatetime,
    BaseModel,
    Field,
    RootModel,
    confloat,
    constr,
)


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


class NavigationStatus(Enum):
    number_0 = 0
    number_1 = 1
    number_2 = 2
    number_3 = 3
    number_4 = 4
    number_5 = 5
    number_6 = 6
    number_7 = 7
    number_8 = 8
    number_9 = 9
    number_10 = 10
    number_11 = 11
    number_12 = 12
    number_13 = 13
    number_14 = 14
    number_15 = 15


class PositionAccuracy(Enum):
    number_0 = 0
    number_1 = 1


class SpecialManeuverIndicator(Enum):
    number_0 = 0
    number_1 = 1
    number_2 = 2


class Type6(Enum):
    Vessel = 'Vessel'


class VesselSubType(Enum):
    number_1 = 1
    number_2 = 2
    number_3 = 3
    number_4 = 4
    number_5 = 5
    number_6 = 6
    number_7 = 7
    number_8 = 8
    number_9 = 9
    number_10 = 10
    number_11 = 11
    number_12 = 12
    number_13 = 13
    number_14 = 14
    number_15 = 15
    number_16 = 16
    number_17 = 17
    number_18 = 18
    number_19 = 19
    number_20 = 20
    number_21 = 21
    number_22 = 22
    number_23 = 23
    number_24 = 24
    number_25 = 25
    number_26 = 26
    number_27 = 27
    number_28 = 28
    number_29 = 29
    number_30 = 30
    number_31 = 31
    number_32 = 32
    number_33 = 33
    number_34 = 34
    number_35 = 35
    number_36 = 36
    number_37 = 37
    number_38 = 38
    number_39 = 39
    number_40 = 40
    number_41 = 41
    number_42 = 42
    number_43 = 43
    number_44 = 44
    number_45 = 45
    number_46 = 46
    number_47 = 47
    number_48 = 48
    number_49 = 49
    number_50 = 50
    number_51 = 51
    number_52 = 52
    number_53 = 53
    number_54 = 54
    number_55 = 55
    number_56 = 56
    number_57 = 57
    number_58 = 58
    number_59 = 59
    number_60 = 60
    number_61 = 61
    number_62 = 62
    number_63 = 63
    number_64 = 64
    number_65 = 65
    number_66 = 66
    number_67 = 67
    number_68 = 68
    number_69 = 69
    number_70 = 70
    number_71 = 71
    number_72 = 72
    number_73 = 73
    number_74 = 74
    number_75 = 75
    number_76 = 76
    number_77 = 77
    number_78 = 78
    number_79 = 79
    number_80 = 80
    number_81 = 81
    number_82 = 82
    number_83 = 83
    number_84 = 84
    number_85 = 85
    number_86 = 86
    number_87 = 87
    number_88 = 88
    number_89 = 89
    number_90 = 90
    number_91 = 91
    number_92 = 92
    number_93 = 93
    number_94 = 94
    number_95 = 95
    number_96 = 96
    number_97 = 97
    number_98 = 98
    number_99 = 99


class VesselType(Enum):
    number_1 = 1
    number_2 = 2
    number_3 = 3
    number_4 = 4
    number_5 = 5
    number_6 = 6
    number_7 = 7
    number_8 = 8
    number_9 = 9


class Vessel(BaseModel):
    address: Optional[Address] = Field(None, description='The mailing address')
    airDraught: Optional[float] = Field(
        None,
        description="Air Draught (distance from the top of a vessel''s highest point to its waterline)",
    )
    alternateName: Optional[str] = Field(
        None, description='An alternative name for this item'
    )
    areaServed: Optional[str] = Field(
        None,
        description='The geographic area where a service or offered item is provided',
    )
    beam: Optional[confloat(ge=0.0, le=1000.0)] = Field(
        None, description='Beam of Vessel'
    )
    buildingAt: Optional[AwareDatetime] = Field(
        None,
        description='Date and time of building of the vessel represented by an ISO 8601 UTC format',
    )
    callSign: Optional[str] = Field(
        None,
        description='Maritime call signs are call signs assigned as unique identifiers to vessels',
    )
    courseOverGround: Optional[float] = Field(
        None, description='Course Over Ground (COG)'
    )
    createdAt: Optional[AwareDatetime] = Field(
        None,
        description='Date and time of creation of the entity represented by an ISO 8601 UTC format',
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
    deadweightTonnage: Optional[float] = Field(
        None, description='Deadweight Tonnage (DWT)'
    )
    description: Optional[str] = Field(None, description='A description of this item')
    destinationPort: Optional[str] = Field(
        None,
        description='Destination Port (Geographic coding scheme UN/LOCODE (United Nations Code for Trade and Transport Locations). https://unece.org/trade/publications/recommendation-ndeg16-united-nations-code-trade-and-transport-locations)',
    )
    draught: Optional[float] = Field(
        None,
        description='Draught (vertical distance between the waterline and the bottom of the hull (keel))',
    )
    estimatedTimeOfArrival: Optional[AwareDatetime] = Field(
        None,
        description='Estimated time of arrival, as it was originally planned and entered by the shipper, represented by an ISO 8601 UTC format',
    )
    financialOwner: Optional[str] = Field(None, description='Financial Owner')
    flagCode: Optional[str] = Field(
        None, description='International Flag Code (ISO 3166-1 alfa-2)'
    )
    grossTonnage: Optional[float] = Field(None, description='Gross Tonnage (GT)')
    heading: Optional[confloat(ge=0.0, le=511.0)] = Field(
        None, description='Heading of the Vessel (HDG)'
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
        description='International Maritime Organization Number (a global forever UID)',
    )
    length: Optional[confloat(ge=0.0, le=8000.0)] = Field(
        None, description='Length of Vessel'
    )
    location: Optional[
        Union[Location, Location1, Location2, Location3, Location4, Location5]
    ] = Field(
        None,
        description='Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon',
    )
    manager: Optional[str] = Field(None, description='Manager Vessel')
    maximumDraught: Optional[float] = Field(None, description='Maximum Draught')
    mmsi: Optional[float] = Field(
        None,
        description="Marine Mobile Service Identity Number (a temporarily assigned UID, issued by that object's current flag state)",
    )
    modifiedAt: Optional[AwareDatetime] = Field(
        None,
        description='Date and time of last modification of the entity represented by an ISO 8601 UTC format',
    )
    name: Optional[str] = Field(None, description='The name of this item')
    navigationStatus: Optional[NavigationStatus] = Field(
        None,
        description="Enum: '0=Under way using engine,1=At anchor,2=Not under command,3=Restricted manoeuverability,4=Constrained by her draught,5=Moored,6=Aground,7=Engaged in Fishing,8=Under way sailing,9=Reserved for future amendment of Navigational Status for HSC,10=Reserved for future amendment of Navigational Status for WIG,11=Reserved for future use,12=Reserved for future use,13=Reserved for future use,14=AIS-SART is active,15=Not defined (default)'. Navigation Status. AIVDM/AIVDO data format",
    )
    observedAt: Optional[AwareDatetime] = Field(
        None,
        description='Date and time of this observation represented by an ISO 8601 UTC format',
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
    ownerVessel: Optional[str] = Field(None, description='Owner Vessel')
    photo: Optional[str] = Field(None, description='Vessel Photo URL')
    positionAccuracy: Optional[PositionAccuracy] = Field(
        None,
        description="global navigation satellite system (GNSS) receiver or of other electronic position fixing device; default),1=High (< 10 m; differential mode of e.g. DGNSS receiver)'. Code for the accuracy of the vessel position flag",
    )
    previousPort: Optional[str] = Field(
        None,
        description='Previous Port (Geographic coding scheme UN/LOCODE (United Nations Code for Trade and Transport Locations). https://unece.org/trade/publications/recommendation-ndeg16-united-nations-code-trade-and-transport-locations)',
    )
    rateOfTurn: Optional[confloat(ge=0.0, le=708.0)] = Field(
        None, description='Rate of Turn (ROT)'
    )
    seeAlso: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None, description='list of uri pointing to additional resources about the item'
    )
    source: Optional[str] = Field(
        None,
        description='A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object',
    )
    specialManeuverIndicator: Optional[SpecialManeuverIndicator] = Field(
        None,
        description="Enum: '0=Not available (default),1=Not engaged in special maneuver,2=Engaged in special maneuver'. Code for the special maneuver flag",
    )
    speedOverGround: Optional[float] = Field(
        None, description='Speed Over Ground (SOG)'
    )
    technicalManager: Optional[str] = Field(None, description='Technical Manager')
    toBow: Optional[float] = Field(None, description='Dimension to Bow')
    toPort: Optional[float] = Field(None, description='Dimension to Port')
    toStardboard: Optional[float] = Field(None, description='Dimension to Starboard')
    toStern: Optional[float] = Field(None, description='Dimension to Stern')
    type: Optional[Type6] = Field(
        None, description='NGSI Entity type. It has to be Vessel'
    )
    vesselSubType: Optional[VesselSubType] = Field(
        None,
        description="Enum: '0=Not available (default),1-19=Reserved for future use,20=Wing in ground (WIG), all ships of this type,21=Wing in ground (WIG), Hazardous category A,22=Wing in ground (WIG), Hazardous category B,23=Wing in ground (WIG), Hazardous category C,24=Wing in ground (WIG), Hazardous category D,25-29=Wing in ground (WIG), Reserved for future use,30=Fishing,31=Towing,32=Towing: length exceeds 200m or breadth exceeds 25m,33=Dredging or underwater ops,34=Diving ops,35=Military ops,36=Sailing,37=Pleasure Craft,38-39=Reserved,40=High speed craft (HSC), all ships of this type,41=High speed craft (HSC), Hazardous category A,42=High speed craft (HSC), Hazardous category B,43=High speed craft (HSC), Hazardous category C,44=High speed craft (HSC), Hazardous category D,45-48=High speed craft (HSC), Reserved for future use,49=High speed craft (HSC), No additional information,50=Pilot Vessel,51=Search and Rescue vessel,52=Tug,53=Port Tender,54=Anti-pollution equipment,55=Law Enforcement,56-57=Spare - Local Vessel,58=Medical Transport,59=Noncombatant ship according to RR Resolution No. 18,60=Passenger, all ships of this type,61=Passenger, Hazardous category A,62=Passenger, Hazardous category B,63=Passenger, Hazardous category C,64=Passenger, Hazardous category D,65-68=Passenger, Reserved for future use,69=Passenger, No additional information,70=Cargo, all ships of this type,71=Cargo, Hazardous category A,72=Cargo, Hazardous category B,73=Cargo, Hazardous category C,74=Cargo, Hazardous category D,75-78=Cargo, Reserved for future use,79=Cargo, No additional information,80=Tanker, all ships of this type,81=Tanker, Hazardous category A,82=Tanker, Hazardous category B,83=Tanker, Hazardous category C,84=Tanker, Hazardous category D,85-88=Tanker, Reserved for future use,89=Tanker, No additional information,90=Other Type, all ships of this type,91=Other Type, Hazardous category A,92=Other Type, Hazardous category B,93=Other Type, Hazardous category C,94=Other Type, Hazardous category D,95-98=Other Type, Reserved for future use,99=Other Type, no additional information'. Code for vessel Sub-Type",
    )
    vesselType: Optional[VesselType] = Field(
        None,
        description="Enum: '1=Reserved,2=Wing In Ground,3=Special Category,4=High-Speed Craft,5=Special Category,6=Passenger,7=Cargo,8=Tanker,9=Other'. Code for vessel type",
    )
