<!-- 10-Header -->
 
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)
 
엔티티: 시설
================
<!-- /10-Header -->
 
<!-- 15-License -->
 
[Open License](https://github.com/smart-data-models//dataModel.MarineTransport/blob/master/Facility/LICENSE.md)
 
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)
<!-- /15-License -->
 
<!-- 20-Description -->
 
글로벌 설명: **이 데이터 모델은 항구 내의 시설을 설명하며, 이에는 부두, 터미널 또는 기타 항구 인프라가 포함될 수 있습니다.**
버전: 0.0.1
<!-- /20-Description -->
 
<!-- 30-PropertiesList -->
 
 
## 속성 목록
 
<sup><sub>[*] 속성에 유형이 없으면 여러 유형이나 다른 형식/패턴을 가질 수 있기 때문입니다</sub></sup>
- `address[object]`: 우편 주소입니다. 모델: [https://schema.org/address](https://schema.org/address)
	- `addressCountry[string]`: 국가입니다. 예를 들어, 스페인입니다. 모델: [https://schema.org/addressCountry](https://schema.org/addressCountry)
	- `addressLocality[string]`: 도로 주소가 있는 지역이며, 이는 지역에 있습니다. 모델: [https://schema.org/addressLocality](https://schema.org/addressLocality)
	- `addressRegion[string]`: 지역은 행정 구역의 유형으로, 일부 국가에서는 지역 정부에서 관리합니다. 모델: [https://schema.org/addressRegion](https://schema.org/addressRegion)
	- `district[string]`: 구역은 행정 구역의 유형으로, 일부 국가에서는 지역 정부에서 관리합니다.
	- `postOfficeBoxNumber[string]`: 우체국 박스 번호입니다. 예를 들어, 03578입니다. 모델: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)
	- `postalCode[string]`: 우편 번호입니다. 예를 들어, 24004입니다. 모델: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)
	- `streetAddress[string]`: 도로 주소입니다. 모델: [https://schema.org/streetAddress](https://schema.org/streetAddress)
	- `streetNr[string]`: 공공 도로에서 특정 속성을 식별하는 번호입니다.
- `alternateName[string]`: 이 항목의 대체 이름입니다.
- `areaServed[string]`: 서비스 또는 제공된 항목이 제공되는 지리적 지역입니다. 모델: [https://schema.org/Text](https://schema.org/Text)
- `bollardCodes[array]`: 시설에서 사용 가능한 볼라드 코드 목록입니다.
- `closed[boolean]`: 시설이 현재 닫혀 있는지 여부를 나타냅니다.
- `dataProvider[string]`: 조화된 데이터 엔티티를 제공하는 제공자의 일련의 문자입니다.
- `dateCreated[date-time]`: 엔티티 생성 타임스탬프입니다. 이는 일반적으로 저장 플랫폼에서 할당됩니다.
- `dateModified[date-time]`: 엔티티의 마지막 수정 타임스탬프입니다. 이는 일반적으로 저장 플랫폼에서 할당됩니다.
- `deadweight[number]`: 시설에서 허용되는 최대 중량입니다.
- `description[string]`: 이 항목에 대한 설명입니다.
- `displacement[number]`: 시설에서 허용되는 최대 배수량입니다.
- `facilityCode[string]`: 시설을 식별하는 코드입니다.
- `facilityName[string]`: 시설의 이름입니다.
- `facilityType[string]`: 시설의 유형입니다. 예를 들어, 부두, 터미널 등입니다.
- `firstBollard[number]`: 시설의 첫 번째 볼라드 식별자입니다.
- `id[*]`: 엔티티의 고유 식별자입니다.
- `lastBollard[number]`: 시설의 마지막 볼라드 식별자입니다.
- `latitude[['number', 'null']]`: 시설 위치의 위도 좌표입니다.
- `location[*]`: 항목에 대한 Geojson 참조입니다. 이는 점, 선, 다각형, 다중 점, 다중 선 또는 다중 다각형일 수 있습니다.
- `longitude[number]`: 시설 위치의 경도 좌표입니다.
- `maxBeam[number]`: 시설에서 허용되는 최대 빔 너비입니다.
- `maxDraught[number]`: 시설에서 허용되는 최대 흘수입니다.
- `maxLoa[number]`: 시설에서 허용되는 최대 길이입니다.
- `minimumProbe[number]`: 시설의 최소 깊이입니다.
- `minimumProbeDate[date-time]`: 최소 깊이가 마지막으로 기록된 날짜입니다.
- `modifiedDate[date-time]`: 시설 엔티티의 마지막 수정 날짜 및 시간입니다.
- `mrn[string]`: MRN 코드 식별자입니다. 이는 엔티티를 잘 알려진 의미와 시작자로 관련시키는 고유 식별자입니다.
    제안된 형식은
    id::='urn:mrn:eshuv:<ONSS>:portcalls:facility:code:[0-9]+' 또는
    OID:= 조직 UN/LOCODE, OONSS:=서비스 제공 조직 이름, 2099는 포트콜이 시작된 연도, 9999999는 고유 식별자입니다.
    예를 들어, urn:mrn:eshuv:portcalls:facility:id:196
     국제 표준에서는 [선박 방문]으로도 알려져 있습니다.
- `name[string]`: 이 항목의 이름입니다.
- `navigationSector[string]`: 이 시설과 관련된 항해 부문입니다.
- `owner[array]`: 소유자(들)의 고유 ID를 참조하는 JSON으로 인코딩된 문자열 시퀀스를 포함하는 목록입니다.
- `planningGroup[string]`: 시설이 속한 계획 그룹입니다.
- `portCode[string]`: 이 시설이 위치한 항구의 코드입니다. 모델: [Unlocode](https://unece.org/trade/cefact/unlocode-code-list-country-and-territory)
- `remarks[string]`: 시설에 대한 추가备注 또는 노트입니다.
- `seeAlso[*]`: 항목에 대한 추가 리소스를 가리키는 URI 목록입니다.
- `source[string]`: 엔티티 데이터의 원래 출처를 URL로 제공하는 문자열 시퀀스입니다. 완전한 도메인 이름이나 출처 객체의 URL을 권장합니다.
- `terminal[string]`: 이 시설과 관련된 터미널의 이름입니다.
- `terminalRef[string]`: 이 시설과 관련된 터미널 엔티티에 대한 참조입니다.
- `type[string]`: NGSI 엔티티 유형입니다. 시설이어야 합니다.
<!-- /30-PropertiesList -->
 
<!-- 35-RequiredProperties -->
 
필수 속성
- `id`
- `portCode`
- `type`
<!-- /35-RequiredProperties -->
 
<!-- 40-NotesYaml -->
 
<!-- /40-NotesYaml -->
 
<!-- 50-DataModelHeader -->
 
## 속성에 대한 데이터 모델 설명
사전순으로 정렬됨 (자세한 정보를 위해 클릭)
<!-- /50-DataModelHeader -->
 
<!-- 60-ModelYaml -->
 
<details><summary><strong>전체 yaml 세부 정보</strong></summary>
 
```yaml  
Facility:    
  description: This data model describes a facility in a port, which may include berths, terminals, or other port infrastructure.    
  properties:    
    address:    
      description: The mailing address    
      properties:    
        addressCountry:    
          description: The country. For example, Spain    
          type: string    
          x-ngsi:    
            model: https://schema.org/addressCountry    
            type: Property    
        addressLocality:    
          description: The locality in which the street address is, and which is in the region    
          type: string    
          x-ngsi:    
            model: https://schema.org/addressLocality    
            type: Property    
        addressRegion:    
          description: The region in which the locality is, and which is in the country    
          type: string    
          x-ngsi:    
            model: https://schema.org/addressRegion    
            type: Property    
        district:    
          description: A district is a type of administrative division that, in some countries, is managed by the local government    
          type: string    
          x-ngsi:    
            type: Property    
        postOfficeBoxNumber:    
          description: The post office box number for PO box addresses. For example, 03578    
          type: string    
          x-ngsi:    
            model: https://schema.org/postOfficeBoxNumber    
            type: Property    
        postalCode:    
          description: The postal code. For example, 24004    
          type: string    
          x-ngsi:    
            model: https://schema.org/https://schema.org/postalCode    
            type: Property    
        streetAddress:    
          description: The street address    
          type: string    
          x-ngsi:    
            model: https://schema.org/streetAddress    
            type: Property    
        streetNr:    
          description: Number identifying a specific property on a public street    
          type: string    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        model: https://schema.org/address    
        type: Property    
    alternateName:    
      description: An alternative name for this item    
      type: string    
      x-ngsi:    
        type: Property    
    areaServed:    
      description: The geographic area where a service or offered item is provided    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    bollardCodes:    
      description: List of bollard codes available at the facility.    
      items:    
        description: Any element in the list of bollard codes available at the facility.    
        type: string    
        x-ngsi:    
          type: Property    
      type: array    
      x-ngsi:    
        type: Property    
    closed:    
      description: Indicates if the facility is currently closed.    
      type: boolean    
      x-ngsi:    
        type: Property    
    dataProvider:    
      description: A sequence of characters identifying the provider of the harmonised data entity    
      type: string    
      x-ngsi:    
        type: Property    
    dateCreated:    
      description: Entity creation timestamp. This will usually be allocated by the storage platform    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateModified:    
      description: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    deadweight:    
      description: Maximum deadweight of vessels allowed in the facility.    
      type: number    
      x-ngsi:    
        type: Property    
    description:    
      description: A description of this item    
      type: string    
      x-ngsi:    
        type: Property    
    displacement:    
      description: Maximum displacement allowed in the facility.    
      type: number    
      x-ngsi:    
        type: Property    
    facilityCode:    
      description: Code identifying the facility.    
      type: string    
      x-ngsi:    
        type: Property    
    facilityName:    
      description: Name of the facility.    
      type: string    
      x-ngsi:    
        type: Property    
    facilityType:    
      description: Type of facility, such as BERTH, TERMINAL, etc.    
      enum:    
        - BERTH    
        - TERMINAL    
        - ANCHORAGE    
        - OTHER    
      type: string    
      x-ngsi:    
        type: Property    
    firstBollard:    
      description: First bollard identifier in the facility.    
      type: number    
      x-ngsi:    
        type: Property    
    id:    
      anyOf:    
        - description: Identifier format of any NGSI entity    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
          x-ngsi:    
            type: Property    
        - description: Identifier format of any NGSI entity    
          format: uri    
          type: string    
          x-ngsi:    
            type: Property    
      description: Unique identifier of the entity    
      x-ngsi:    
        type: Relationship    
    lastBollard:    
      description: Last bollard identifier in the facility.    
      type: number    
      x-ngsi:    
        type: Property    
    latitude:    
      description: Latitude coordinate of the facility location.    
      type:    
        - number    
        - 'null'    
      x-ngsi:    
        type: Property    
    location:    
      description: Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon    
      oneOf:    
        - description: Geojson reference to the item. Point    
          properties:    
            bbox:    
              description: BBox of the  Point    
              items:    
                type: number    
              minItems: 4    
              type: array    
              x-ngsi:    
                type: Property    
            coordinates:    
              description: Coordinates of the Point    
              items:    
                type: number    
              minItems: 2    
              type: array    
              x-ngsi:    
                type: Property    
            type:    
              enum:    
                - Point    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON Point    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. LineString    
          properties:    
            bbox:    
              description: BBox coordinates of the LineString    
              items:    
                type: number    
              minItems: 4    
              type: array    
              x-ngsi:    
                type: Property    
            coordinates:    
              description: Coordinates of the LineString    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              minItems: 2    
              type: array    
              x-ngsi:    
                type: Property    
            type:    
              enum:    
                - LineString    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON LineString    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. Polygon    
          properties:    
            bbox:    
              description: BBox coordinates of the Polygon    
              items:    
                type: number    
              minItems: 4    
              type: array    
              x-ngsi:    
                type: Property    
            coordinates:    
              description: Coordinates of the Polygon    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 4    
                type: array    
              type: array    
              x-ngsi:    
                type: Property    
            type:    
              enum:    
                - Polygon    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON Polygon    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. MultiPoint    
          properties:    
            bbox:    
              description: BBox coordinates of the LineString    
              items:    
                type: number    
              minItems: 4    
              type: array    
              x-ngsi:    
                type: Property    
            coordinates:    
              description: Coordinates of the MulitPoint    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              type: array    
              x-ngsi:    
                type: Property    
            type:    
              enum:    
                - MultiPoint    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON MultiPoint    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. MultiLineString    
          properties:    
            bbox:    
              description: BBox coordinates of the LineString    
              items:    
                type: number    
              minItems: 4    
              type: array    
              x-ngsi:    
                type: Property    
            coordinates:    
              description: Coordinates of the MultiLineString    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 2    
                type: array    
              type: array    
              x-ngsi:    
                type: Property    
            type:    
              enum:    
                - MultiLineString    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON MultiLineString    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. MultiLineString    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              description: Coordinates of the MultiPolygon    
              items:    
                items:    
                  items:    
                    items:    
                      type: number    
                    minItems: 2    
                    type: array    
                  minItems: 4    
                  type: array    
                type: array    
              type: array    
              x-ngsi:    
                type: Property    
            type:    
              enum:    
                - MultiPolygon    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON MultiPolygon    
          type: object    
          x-ngsi:    
            type: GeoProperty    
      x-ngsi:    
        type: GeoProperty    
    longitude:    
      description: Longitude coordinate of the facility location.    
      type: number    
      x-ngsi:    
        type: Property    
    maxBeam:    
      description: Maximum beam width of vessels allowed in meters.    
      type: number    
      x-ngsi:    
        type: Property    
    maxDraught:    
      description: Maximum draught allowed in meters.    
      type: number    
      x-ngsi:    
        type: Property    
    maxLoa:    
      description: Maximum length overall (LOA) of vessels allowed in meters.    
      type: number    
      x-ngsi:    
        type: Property    
    minimumProbe:    
      description: Minimum depth of the facility in meters.    
      type: number    
      x-ngsi:    
        type: Property    
    minimumProbeDate:    
      description: Date when the minimum depth was last recorded.    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    modifiedDate:    
      description: Date and time of last modification of the facility entity.    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    mrn:    
      description: "MRN coded identifier. It has to be related to the entity in a way that is well-known by different organisms the meaning and the initiator of the entity, and all next parties will maintain on its origianl value. This identifier must be an UNIQUE identifier of the PortCall entity assigned by the system who created on first the entity. This URN should Conforms MRN & IETF specifically RFC 2141, RFC 5234, and RFC 8141. \n    The propossed format is \n    id::='urn:mrn:eshuv:<ONSS>:portcalls:facility:code:[0-9]+' or  \n    where OID:= Organisation UN/LOCODE, OONSS:=Organization Name of Service, 2099 the year on which the portcall was initiated, 9999999 an increasing, unique identifier that the issuer of the Facility entity will identify on his sistems (i.e. a SQL row-id), \n    i.e. urn:mrn:eshuv:portcalls:facility:id:196 \n     See [Unlocode](https://unece.org/trade/cefact/unlocode-code-list-country-and-territory)In international standards is also known as [Ship's Visit]"    
      enum:    
        - PortCall    
      type: string    
      x-ngsi:    
        type: Property    
    name:    
      description: The name of this item    
      type: string    
      x-ngsi:    
        type: Property    
    navigationSector:    
      description: Navigation sector associated with this facility.    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)    
      items:    
        anyOf:    
          - description: Identifier format of any NGSI entity    
            maxLength: 256    
            minLength: 1    
            pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
            type: string    
            x-ngsi:    
              type: Property    
          - description: Identifier format of any NGSI entity    
            format: uri    
            type: string    
            x-ngsi:    
              type: Property    
        description: Unique identifier of the entity    
        x-ngsi:    
          type: Relationship    
      type: array    
      x-ngsi:    
        type: Property    
    planningGroup:    
      description: Planning group to which the facility belongs.    
      type: string    
      x-ngsi:    
        type: Property    
    portCode:    
      description: Code of the port where this facility is located.    
      type: string    
      x-ngsi:    
        type: Property    
    remarks:    
      description: Additional remarks or notes about the facility.    
      type: string    
      x-ngsi:    
        type: Property    
    seeAlso:    
      description: list of uri pointing to additional resources about the item    
      oneOf:    
        - items:    
            format: uri    
            type: string    
          minItems: 1    
          type: array    
        - format: uri    
          type: string    
      x-ngsi:    
        type: Property    
    source:    
      description: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object    
      type: string    
      x-ngsi:    
        type: Property    
    terminal:    
      description: Name of the terminal associated with this facility.    
      type: string    
      x-ngsi:    
        type: Property    
    terminalRef:    
      description: Reference to the terminal entity associated with this facility.    
      type: string    
      x-ngsi:    
        type: Property    
    type:    
      description: NGSI Entity type. It has to be Facility    
      enum:    
        - Facility    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - portCode    
    - type    
  type: object    
  x-derived-from: ''    
  x-disclaimer: Redistribution and use in source and binary forms...    
  x-license-url: https://github.com/smart-data-models/dataModel.MarineTransport/blob/master/Facility/LICENSE.md    
  x-model-schema: https://raw.githubusercontent.com/smart-data-models/dataModel.MarineTransport/master/Facility/schema.json    
  x-model-tags: ESHUV    
  x-version: 0.0.1    
```
</details>
 
<!-- /60-ModelYaml -->
 
<!-- 70-MiddleNotes -->
 
<!-- /70-MiddleNotes -->
 
<!-- 80-Examples -->
 
## 예제 페이로드
 
#### 시설 NGSI-v2 키-값 예제
시설의 JSON 형식의 키-값 예입니다. 이는 NGSI-v2와 호환되며 `options=keyValues`를 사용하여 개별 엔티티의 컨텍스트 데이터를 반환합니다.
<details><summary><strong>예제 표시/숨기기</strong></summary>
 
```json  
{  
  "id": "urn:mrn:eshuv:facilities:facility:code:20",  
  "type": "Facility",  
  "portCode": "ESVLC",  
  "facilityName": "Levante pesquero",  
  "facilityCode": "0011",  
  "facilityType": "BERTH",  
  "terminal": "Levante",  
  "terminalRef": "urn:mrn:eshuv:infrastructure:terminal:code:20",  
  "planningGroup": "Levante",  
  "navigationSector": "CINT",  
  "minimumProbe": 2.4,  
  "minimumProbeDate": "2024-12-01T00:00:00",  
  "displacement": 103500.00,  
  "latitude": 37.252290,  
  "longitude": -6.958843,  
  "deadweight": 35000.00,  
  "maxDraught": 4.0,  
  "maxLoa": 240.0,  
  "maxBeam": 36.50,  
  "remarks": "Levante pesquero",  
  "firstBollard": 1,  
  "lastBollard": 34,  
  "closed": false,  
  "bollardCodes" : [ "1", "2", "3", "4", "5" ]  
}  
```
</details>
 
#### 시설 NGSI-v2 정규화된 예제
시설의 JSON 형식의 정규화된 예입니다. 이는 NGSI-v2와 호환되며 옵션을 사용하지 않고 개별 엔티티의 컨텍스트 데이터를 반환합니다.
<details><summary><strong>예제 표시/숨기기</strong></summary>
 
```json  
{  
  "id": "urn:mrn:eshuv:facilities:facility:code:20",  
  "type": "Facility",  
  "portCode": {  
    "type": "Text",  
    "value": "ESVLC"  
  },  
  "facilityName": {  
    "type": "Text",  
    "value": "Levante pesquero"  
  },  
  "facilityCode": {  
    "type": "Text",  
    "value": "0011"  
  },  
  "facilityType": {  
    "type": "Text",  
    "value": "BERTH"  
  },  
  "terminal": {  
    "type": "Text",  
    "value": "Levante"  
  },  
  "terminalRef": {  
    "type": "Text",  
    "value": "urn:mrn:eshuv:infrastructure:terminal:code:20"  
  },  
  "planningGroup": {  
    "type": "Text",  
    "value": "Levante"  
  },  
  "navigationSector": {  
    "type": "Text",  
    "value": "CINT"  
  },  
  "minimumProbe": {  
    "type": "Number",  
    "value": 2.4  
  },  
  "minimumProbeDate": {  
    "type": "DateTime",  
    "value": "2024-12-01T00:00:00"  
  },  
  "displacement": {  
    "type": "Number",  
    "value": 103500.0  
  },  
  "latitude": {  
    "type": "Number",  
    "value": 37.25229  
  },  
  "longitude": {  
    "type": "Number",  
    "value": -6.958843  
  },  
  "deadweight": {  
    "type": "Number",  
    "value": 35000.0  
  },  
  "maxDraught": {  
    "type": "Number",  
    "value": 4.0  
  },  
  "maxLoa": {  
    "type": "Number",  
    "value": 240.0  
  },  
  "maxBeam": {  
    "type": "Number",  
    "value": 36.5  
  },  
  "remarks": {  
    "type": "Text",  
    "value": "Levante pesquero"  
  },  
  "firstBollard": {  
    "type": "Number",  
    "value": 1  
  },  
  "lastBollard": {  
    "type": "Number",  
    "value": 34  
  },  
  "closed": {  
    "type": "Boolean",  
    "value": false  
  },  
  "bollardCodes": {  
    "type": "Array",  
    "value": [  
      "1",  
      "2",  
      "3",  
      "4",  
      "5"  
    ]  
  }  
}  
```
</details>
 
#### 시설 NGSI-LD 키-값 예제
시설의 JSON-LD 형식의 키-값 예입니다. 이는 NGSI-LD와 호환되며 `options=keyValues`를 사용하여 개별 엔티티의 컨텍스트 데이터를 반환합니다.
<details><summary><strong>예제 표시/숨기기</strong></summary>
 
```json  
{  
  "id": "urn:ngsi-ld:Facility:urn:mrn:eshuv:facilities:facility:code:20",  
  "type": "Facility",  
  "portCode": "ESVLC",  
  "facilityName": "Levante pesquero",  
  "facilityCode": "0011",  
  "facilityType": "BERTH",  
  "terminal": "Levante",  
  "terminalRef": "urn:mrn:eshuv:infrastructure:terminal:code:20",  
  "planningGroup": "Levante",  
  "navigationSector": "CINT",  
  "minimumProbe": 2.4,  
  "minimumProbeDate": "2024-12-01T00:00:00",  
  "displacement": 103500.0,  
  "latitude": 37.25229,  
  "longitude": -6.958843,  
  "deadweight": 35000.0,  
  "maxDraught": 4.0,  
  "maxLoa": 240.0,  
  "maxBeam": 36.5,  
  "remarks": "Levante pesquero",  
  "firstBollard": 1,  
  "lastBollard": 34,  
  "closed": false,  
  "bollardCodes": [  
    "1",  
    "2",  
    "3",  
    "4",  
    "5"  
  ],  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.Ports/master/context.jsonld"  
  ]  
}  
```
</details>
 
#### 시설 NGSI-LD 정규화된 예제
시설의 JSON-LD 형식의 정규화된 예입니다. 이는 NGSI-LD와 호환되며 옵션을 사용하지 않고 개별 엔티티의 컨텍스트 데이터를 반환합니다.
<details><summary><strong>예제 표시/숨기기</strong></summary>
 
```json  
{  
  "id": "urn:ngsi-ld:Facility:urn:mrn:eshuv:facilities:facility:code:20",  
  "type": "Facility",  
  "portCode": {  
    "type": "Property",  
    "value": "ESVLC"  
  },  
  "facilityName": {  
    "type": "Property",  
    "value": "Levante pesquero"  
  },  
  "facilityCode": {  
    "type": "Property",  
    "value": "0011"  
  },  
  "facilityType": {  
    "type": "Property",  
    "value": "BERTH"  
  },  
  "terminal": {  
    "type": "Property",  
    "value": "Levante"  
  },  
  "terminalRef": {  
    "type": "Property",  
    "value": "urn:mrn:eshuv:infrastructure:terminal:code:20"  
  },  
  "planningGroup": {  
    "type": "Property",  
    "value": "Levante"  
  },  
  "navigationSector": {  
    "type": "Property",  
    "value": "CINT"  
  },  
  "minimumProbe": {  
    "type": "Property",  
    "value": 2.4  
  },  
  "minimumProbeDate": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2024-12-01T00:00:00"  
    }  
  },  
  "displacement": {  
    "type": "Property",  
    "value": 103500.0  
  },  
  "latitude": {  
    "type": "Property",  
    "value": 37.25229  
  },  
  "longitude": {  
    "type": "Property",  
    "value": -6.958843  
  },  
  "deadweight": {  
    "type": "Property",  
    "value": 35000.0  
  },  
  "maxDraught": {  
    "type": "Property",  
    "value": 4.0  
  },  
  "maxLoa": {  
    "type": "Property",  
    "value": 240.0  
  },  
  "maxBeam": {  
    "type": "Property",  
    "value": 36.5  
  },  
  "remarks": {  
    "type": "Property",  
    "value": "Levante pesquero"  
  },  
  "firstBollard": {  
    "type": "Property",  
    "value": 1  
  },  
  "lastBollard": {  
    "type": "Property",  
    "value": 34  
  },  
  "closed": {  
    "type": "Property",  
    "value": false  
  },  
  "bollardCodes": {  
    "type": "Property",  
    "value": [  
      "1",  
      "2",  
      "3",  
      "4",  
      "5"  
    ]  
  },  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.Ports/master/context.jsonld"  
  ]  
}  
```
</details><!-- /80-Examples -->
 
<!-- 90-FooterNotes -->
 
<!-- /90-FooterNotes -->
 
<!-- 95-Units -->
 
크기 단위에 대한 처리 방법에 대한 답변을 얻으려면 [FAQ 10](https://smartdatamodels.org/index.php/faqs/)를 참조하십시오.
<!-- /95-Units -->
 
<!-- 97-LastFooter -->
 
---
 
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->