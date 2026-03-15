<!-- 10-Header -->
 
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)
 
엔티티: KeyVessel
=================
<!-- /10-Header -->
 
<!-- 15-License -->
 
[Open License](https://github.com/smart-data-models//dataModel.MarineTransport/blob/master/KeyVessel/LICENSE.md)
 
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)
<!-- /15-License -->
 
<!-- 20-Description -->
 
글로벌 설명: **데이터 모델은 항구 커뮤니티가 다음 날에 집중해야 하는 주요 선박에 대한 정보를 제공하기 위한 것입니다. 각 선박의 속성을 나타낼 수 있습니다: 정적 및 동적 정보**
 
버전: 0.0.1
<!-- /20-Description -->
 
<!-- 30-PropertiesList -->
 
 
## 속성 목록
 
<sup><sub>[*] 속성에 유형이 없으면 여러 유형이나 다른 형식/패턴을 가질 수 있습니다</sub></sup>
- `address[object]`: 우편 주소. 모델: [https://schema.org/address](https://schema.org/address)
	- `addressCountry[string]`: 국가. 예: 스페인. 모델: [https://schema.org/addressCountry](https://schema.org/addressCountry)
	- `addressLocality[string]`: 지역의 거리 주소이며, 지역에 있습니다. 모델: [https://schema.org/addressLocality](https://schema.org/addressLocality)
	- `addressRegion[string]`: 지역의 지역이며, 국가에 있습니다. 모델: [https://schema.org/addressRegion](https://schema.org/addressRegion)
	- `district[string]`: 일부 국가에서 지자체가 관리하는 행정 구역 유형입니다.
	- `postOfficeBoxNumber[string]`: 우체국 박스 번호. 예: 03578. 모델: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)
	- `postalCode[string]`: 우편 번호. 예: 24004. 모델: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)
	- `streetAddress[string]`: 거리 주소. 모델: [https://schema.org/streetAddress](https://schema.org/streetAddress)
	- `streetNr[string]`: 공공 도로에서 특정 속성을 식별하는 번호입니다.
- `alternateName[string]`: 이 항목의 대체 이름입니다.
- `areaServed[string]`: 서비스 또는 제공된 항목이 제공되는 지리적 영역입니다. 모델: [https://schema.org/Text](https://schema.org/Text)
- `callSign[string]`: 해상 호출 부호는 선박에 고유 식별자로 할당된 호출 부호입니다. 모델: [https://schema.org/Text](https://schema.org/Text)
- `courseOverGround[number]`: 지상 경로(코그). 모델: [https://schema.org/Number](https://schema.org/Number)
- `createdDate[date-time]`: 엔티티 생성 날짜 및 시간(ISO 8601 UTC 형식). 모델: [https://schema.org/Text](https://schema.org/Text)
- `dataProvider[string]`: 조화된 데이터 엔티티 제공者的 고유 식별자입니다. 모델: [https://schema.org/Text](https://schema.org/Text)
- `dateCreated[date-time]`: 엔티티 생성 타임스탬프. 보통 저장 플랫폼에서 할당됩니다.
- `dateModified[date-time]`: 엔티티의 마지막 수정 타임스탬프. 보통 저장 플랫폼에서 할당됩니다.
- `deletedDate[date-time]`: 엔티티 삭제 날짜 및 시간(ISO 8601 UTC 형식). 모델: [https://schema.org/Text](https://schema.org/Text)
- `description[string]`: 이 항목에 대한 설명입니다.
- `etaAis[date-time]`: 예상 도착 시간(AIS 시스템에서 보고됨). ISO 8601 UTC 형식. 모델: [https://schema.org/Text](https://schema.org/Text)
- `etaAlgorithm[date-time]`: 예상 도착 시간(선박 위치를 기반으로 하는 알고리즘으로 계산됨). ISO 8601 UTC 형식. 모델: [https://schema.org/Text](https://schema.org/Text)
- `flagCode[string]`: 해상 호출 부호는 선박에 고유 식별자로 할당된 호출 부호입니다. 모델: [https://schema.org/Text](https://schema.org/Text)
- `id[*]`: 엔티티의 고유 식별자입니다.
- `imo[number]`: 국제 해사 기구 번호(전 세계적으로 영구적으로 고유한 식별자). 모델: [https://schema.org/Number](https://schema.org/Number)
- `lastPortCode[string]`: 마지막 항구 호출 코드. 코드는 이전 항구를 나타내며, 사용할 수 있습니다. [EMSWe: DE-005-05] [EDIFACT:LOC-3227-92] [IMO:IMO0076]. 모델: [https://schema.org/Text](https://schema.org/Text)
- `latitude[number]`: 선박의 위도 좌표입니다.
- `location[*]`: 지오json 참조는 선박의 위치를 나타냅니다. 관찰 날짜에 선박이 있었던 지점을 나타내는 포인트여야 합니다.
- `longitude[number]`: 선박의 경도 좌표입니다.
- `mmsi[number]`: 해상 이동 서비스 식별 번호(일시적으로 할당된 UID, 현재 국적 국가에서 발급됨). 모델: [https://schema.org/Number](https://schema.org/Number)
- `modifiedDate[date-time]`: 엔티티의 마지막 수정 날짜 및 시간(ISO 8601 UTC 형식). 모델: [https://schema.org/Text](https://schema.org/Text)
- `name[string]`: 이 항목의 이름입니다.
- `navigationStatus[number]`: 열거형: '0=엔진 사용 중, 1=錨, 2=지휘 불가, 3=제한된 기동성, 4=제한된 기동성, 5=계류 중, 6=좌초, 7=어업 중, 8=항해 중, 9=예약됨, 10=예약됨, 11=예약됨, 12=예약됨, 13=예약됨, 14=AIS-SART 활성화, 15=정의되지 않음(기본값)'. 항해 상태. AIVDM/AIVDO 데이터 형식. 모델: [https://schema.org/Number](https://schema.org/Number)
- `nextPortCode[string]`: 다음 항구 호출 코드. 코드는 다음 항구를 나타내며, 사용할 수 있습니다. [EMSWe: DE-005-07] [EDIFACT:LOC-3227-61] [IMO:IMO0120]. 모델: [https://schema.org/Text](https://schema.org/Text)
- `observedDate[date-time]`: 관찰 날짜 및 시간(ISO 8601 UTC 형식). 모델: [https://schema.org/Text](https://schema.org/Text)
- `owner[array]`: JSON으로 인코딩된 문자열 시퀀스를 포함하는 목록으로, 소유자의 고유 ID를 참조합니다.
- `portCallNumber[string]`: 항구 호출 식별자(MRN 형식). 첫 번째 요소는 항구의 5자리 [Unlocode](https://unece.org/trade/cefact/unlocode-code-list-country-and-territory)여야 하며, 연도와 연도별로 고유한 순차 번호로 끝나야 합니다(예: LLLLLYYYY99999). UN/LOCODE의 약어를 사용할 수 있습니다(예: H202310323). 항구 호출 번호는 방문 초기에 할당되지만, 처음에는 null일 수 있습니다. 국제 표준에서는 [Port Call ID], [Visit ID] 또는 [Port Call Coded]라고도 합니다. [EMSWe: DG-004/DG-004-01] [EDIFACT:BGM-1004] [IALA_S211:portCallId] [IMO:IMO108+IMO0153]. 모델: [https://schema.org/Text](https://schema.org/Text)
- `portCallRef[uri]`: 부모 PortCall 엔티티 참조. [NGSI-MarineTransport.PortCall.id]
- `portCode[string]`: 통상 및 운송 위치를 위한 [Unlocode](https://unece.org/trade/cefact/unlocode-code-list-country-and-territory). [EMSWe: DE-004-04] [EDIFACT:LOC-3227-153] [IALA_S211:portCode] [IMO:IMO0108]. 모델: [https://schema.org/Text](https://schema.org/Text)
- `positionAccuracy[number]`: 열거형: '0=저(> 10m; 자율 모드; 예: GNSS 수신기 또는 기타 전자 위치 고정 장치의 기본값), 1=고( < 10m; 예: DGNSS 수신기의 차동 모드)'. 선박 위치 정확도 플래그 코드. 모델: [https://schema.org/Number](https://schema.org/Number)
- `seeAlso[*]`: 항목에 대한 추가 리소스를 가리키는 URI 목록입니다.
- `source[string]`: 엔티티 데이터의 원래 출처를 URL로 제공하는 문자열 시퀀스입니다. 출처 제공자의 완전한 도메인 이름이나 출처 객체의 URL을 권장합니다.
- `speedOverGround[number]`: 지상 속도(SOG). 모델: [https://schema.org/Number](https://schema.org/Number)
- `type[string]`: NGSI 엔티티 유형. KeyVessel이어야 합니다.
- `vesselAtPort[boolean]`: 선박이 항구 한계 내에 있습니다. 대기 중, 항구 입구에서 기다리는 중, 지시를 기다리는 중 등. 모델: [https://schema.org/Boolean](https://schema.org/Boolean)
- `vesselName[string]`: 선박 이름. 모델: [https://schema.org/Text](https://schema.org/Text)
- `vesselRef[uri]`: 부모 MasterVessel 엔티티 참조. [NGSI-MarineTransport.MasterVessel.id]- urn:mrn:<oid>:portcalls:mastervessel:id:9999
<!-- /30-PropertiesList -->
 
<!-- 35-RequiredProperties -->
 
필수 속성
- `id`
- `type`
<!-- /35-RequiredProperties -->
 
<!-- 40-NotesYaml -->
 
<!-- /40-NotesYaml -->
 
<!-- 50-DataModelHeader -->
 
## 속성 데이터 모델 설명
 
알파벳 순으로 정렬됨(클릭하여 세부 정보 보기)
<!-- /50-DataModelHeader -->
 
<!-- 60-ModelYaml -->
 
<details><summary><strong>전체 yaml 세부 정보</strong></summary>
 
```yaml  
KeyVessel:    
  description: 'The data model is intended to provide information about key vessels that a port community must focus his work on next days. It allows to represent the properties of each vessel: static and dynamic information'    
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
    callSign:    
      description: Maritime call signs are call signs assigned as unique identifiers to vessels    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    courseOverGround:    
      description: Course Over Ground (COG)    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: degree    
    createdDate:    
      description: Date and time of creation of the entity represented by an ISO 8601 UTC format    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    dataProvider:    
      description: A sequence of characters identifying the provider of the harmonised data entity    
      enum:    
        - AIS    
        - AISHUB    
        - ALGORITHM    
        - IA    
        - MARINETRAFFIC    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
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
    deletedDate:    
      description: Date and time of deletion of the entity represented by an ISO 8601 UTC format    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    description:    
      description: A description of this item    
      type: string    
      x-ngsi:    
        type: Property    
    etaAis:    
      description: Estimated time of arrival, as it is reported by AIS system, represented by an ISO 8601 UTC format    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    etaAlgorithm:    
      description: Estimated time of arrival, computed by an algorithm based on vessel's positions, represented by an ISO 8601 UTC format    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    flagCode:    
      description: Maritime call signs are call signs assigned as unique identifiers to vessels    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
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
    imo:    
      description: International Maritime Organization Number (a global forever UID)    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    lastPortCode:    
      description: 'Last port of call, coded.The code representing the port immediately previous to the port of arrival, if available. [EMSWe: DE-005-05] [EDIFACT:LOC-3227-92] [IMO:IMO0076] '    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    latitude:    
      description: Latitude coordinate of the vessel    
      type: number    
      x-ngsi:    
        type: Property    
    location:    
      '@id': http://uri.etsi.org/ngsi-ld/location    
      '@type': https://uri.etsi.org/ngsi-ld/GeoProperty    
      description: Geojson reference to the vessel position. It must be a Point where the vessel was placed at observedDate date    
      x-ngsi:    
        type: GeoProperty    
    longitude:    
      description: Longitude coordinate of the vessel    
      type: number    
      x-ngsi:    
        type: Property    
    mmsi:    
      description: Marine Mobile Service Identity Number (a temporarily assigned UID, issued by that object's current flag state)    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    modifiedDate:    
      description: Date and time of last modification of the entity represented by an ISO 8601 UTC format    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    name:    
      description: The name of this item    
      type: string    
      x-ngsi:    
        type: Property    
    navigationStatus:    
      description: Enum:'0=Under way using engine, 1=At anchor, 2=Not under command, 3=Restricted manoeuverability,4=Constrained by her draught, 5=Moored, 6=Aground, 7=Engaged in Fishing, 8=Under way sailing, 9=Reserved for future amendment of Navigational state for HSC, 10=Reserved for future amendment of Navigational Status for WIG, 11=Reserved for future use, 12=Reserved for future use,13=Reserved for future use, 14=AIS-SART is active, 15=Not defined (default)'. Navigation Status. AIVDM/AIVDO data format'    
      enum:    
        - 0    
        - 1    
        - 2    
        - 3    
        - 4    
        - 5    
        - 6    
        - 7    
        - 8    
        - 9    
        - 10    
        - 11    
        - 12    
        - 13    
        - 14    
        - 15    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    nextPortCode:    
      description: 'Next port of call, coded.The code representing the port immediately previous to the port of arrival, if available.. Related to IALA_S211:nestPortCallCod / IMO. [EMSWe: DE-005-07] [EDIFACT:LOC-3227-61] [IMO:IMO0120]'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    observedDate:    
      description: Date and time of this observation represented by an ISO 8601 UTC format    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
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
    portCallNumber:    
      description: 'Port call identifier in MRN format. First element of the NSS should be the 5 character UN/Locode of the port, later the YEAR and finishing with a sequential number in this port [LLLLLYYYY99999] where LLLLL is the UN/LOCODE of the visited port, YYYY is the year, and 99999 is a unique sequential number assigned by port authority unique on each year (i.e. ESHUV202310323). An abbreviation can be used for UN/LOCODE (i.e. H202310323). The portCallNumber is assigned during the initial steps of the visit, but could be null at the beginning. In international standards is also known as [Port Call ID], [Visit ID] or [Port Call Coded]. See [Unlocode](https://unece.org/trade/cefact/unlocode-code-list-country-and-territory) [EMSWe: DG-004/DG-004-01] [EDIFACT:BGM-1004] [IALA_S211:portCallId] [IMO:IMO108+IMO0153]'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    portCallRef:    
      description: Reference to parent PortCall entity. [NGSI-MarineTransport.PortCall.id]    
      format: uri    
      type: string    
      x-ngsi:    
        type: Relationship    
    portCode:    
      description: 'United Nations Code for Trade and Transport Locations. See [Unlocode](https://unece.org/trade/cefact/unlocode-code-list-country-and-territory) [EMSWe: DE-004-04] [EDIFACT:LOC-3227-153] [IALA_S211:portCode] [IMO:IMO0108] '    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    positionAccuracy:    
      description: Enum:'0=Low (> 10 m; autonomous mode of e.g.global navigation satellite system (GNSS) receiver or of other electronic position fixing device; default), 1=High (< 10 m; differential mode of e.g.DGNSS receiver)'. Code for the accuracy of the vessel position flag    
      enum:    
        - 0    
        - 1    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
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
    speedOverGround:    
      description: Speed Over Ground (SOG)    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: meters per second    
    type:    
      description: NGSI Entity type. It has to be KeyVessel    
      enum:    
        - KeyVessel    
      type: string    
      x-ngsi:    
        type: Property    
    vesselAtPort:    
      description: The vessel is in port limits, including waiting outside, at the harbor entrance, awaiting instructions, etc    
      type: boolean    
      x-ngsi:    
        model: https://schema.org/Boolean    
        type: Property    
    vesselName:    
      description: Vessel Name    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    vesselRef:    
      description: Reference to parent MasterVessel entity. [NGSI-MarineTransport.MasterVessel.id]- urn:mrn:<oid>:portcalls:mastervessel:id:9999    
      format: uri    
      type: string    
      x-ngsi:    
        type: Relationship    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: ''    
  x-disclaimer: Redistribution and use in source and binary forms...    
  x-license-url: https://github.com/smart-data-models/dataModel.MarineTransport/blob/master/KeyVessel/LICENSE.md    
  x-model-schema: https://raw.githubusercontent.com/smart-data-models/dataModel.MarineTransport/master/VesselAtPort/schema.json    
  x-model-tags: I4Trust    
  x-version: 0.0.1    
```
</details>
 
<!-- /60-ModelYaml -->
 
<!-- 70-MiddleNotes -->
 
<!-- /70-MiddleNotes -->
 
<!-- 80-Examples -->
 
## 예제 페이로드
 
#### KeyVessel NGSI-v2 키-값 예제
 
KeyVessel의 JSON 형식의 키-값 예입니다. NGSI-v2와 호환되며 `options=keyValues`을 사용하여 개별 엔티티의 컨텍스트 데이터를 반환합니다.
<details><summary><strong>예제 보기/숨기기</strong></summary>
 
```json  
{  
  "id": "urn:mrn:eshuv:portcalls:portcallvessel:id:1234",  
  "type": "KeyVessel",  
  "vesselRef": "urn:mrn:eshuv:portcalls:mastervessel:imo:9863637",  
  "imo": 9863637,  
  "mmsi": 210049000,  
  "callSign": "5BPC3",  
  "flagCode": "ES",  
  "vesselName": "ELEANOR R.",  
  "portCode":   "ESHUV",  
  "lastPortCode": "ESPMI",  
  "nextPortCode": "ESVLC",  
  "portCallNumber": "ESHUV202401233",  
  "portCallRef": "urn:mrn:eshuv:portcalls:portcall:code:1233",  
  "dataProvider": "AIS",  
  "latitude": 37.2614,  
  "longitude":  -6.9447,  
  "speedOverGround": 11.3,  
  "courseOverGround": 122,  
  "navigationStatus": 4,  
  "observedDate": "2024-07-01T03:11:32Z",  
  "modifiedDate": "2024-07-01T03:07:12Z",  
  "createdDate": "2023-06-03T07:00:00Z",  
  "deletedDate": "2024-07-01T03:07:12Z"  
}  
```
</details>
 
#### KeyVessel NGSI-v2 정규화 예제
 
KeyVessel의 JSON 형식의 정규화 예입니다. NGSI-v2와 호환되며 옵션을 사용하지 않고 개별 엔티티의 컨텍스트 데이터를 반환합니다.
<details><summary><strong>예제 보기/숨기기</strong></summary>
 
```json  
{  
  "id": "urn:mrn:eshuv:portcalls:portcallvessel:id:1234",  
  "type": "KeyVessel",  
  "vesselRef": {  
    "type": "Text",  
    "value": "urn:mrn:eshuv:portcalls:mastervessel:imo:9863637"  
  },  
  "imo": {  
    "type": "Number",  
    "value": 9863637  
  },  
  "mmsi": {  
    "type": "Number",  
    "value": 210049000  
  },  
  "callSign": {  
    "type": "Text",  
    "value": "5BPC3"  
  },  
  "flagCode": {  
    "type": "Text",  
    "value": "ES"  
  },  
  "vesselName": {  
    "type": "Text",  
    "value": "ELEANOR R."  
  },  
  "portCode": {  
    "type": "Text",  
    "value": "ESHUV"  
  },  
  "lastPortCode": {  
    "type": "Text",  
    "value": "ESPMI"  
  },  
  "nextPortCode": {  
    "type": "Text",  
    "value": "ESVLC"  
  },  
  "portCallNumber": {  
    "type": "Text",  
    "value": "ESHUV202401233"  
  },  
  "portCallRef": {  
    "type": "Text",  
    "value": "urn:mrn:eshuv:portcalls:portcall:code:1233"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "AIS"  
  },  
  "latitude": {  
    "type": "Number",  
    "value": 37.2614  
  },  
  "longitude": {  
    "type": "Number",  
    "value": -6.9447  
  },  
  "speedOverGround": {  
    "type": "Number",  
    "value": 11.3  
  },  
  "courseOverGround": {  
    "type": "Number",  
    "value": 122  
  },  
  "navigationStatus": {  
    "type": "Number",  
    "value": 4  
  },  
  "observedDate": {  
    "type": "DateTime",  
    "value": "2024-07-01T03:11:32Z"  
  },  
  "modifiedDate": {  
    "type": "DateTime",  
    "value": "2024-07-01T03:07:12Z"  
  },  
  "createdDate": {  
    "type": "DateTime",  
    "value": "2023-06-03T07:00:00Z"  
  },  
  "deletedDate": {  
    "type": "DateTime",  
    "value": "2024-07-01T03:07:12Z"  
  }  
}  
```
</details>
 
#### KeyVessel NGSI-LD 키-값 예제
 
KeyVessel의 JSON-LD 형식의 키-값 예입니다. NGSI-LD와 호환되며 `options=keyValues`을 사용하여 개별 엔티티의 컨텍스트 데이터를 반환합니다.
<details><summary><strong>예제 보기/숨기기</strong></summary>
 
```json  
{  
  "id": "urn:ngsi-ld:KeyVessel:urn:mrn:eshuv:portcalls:portcallvessel:id:1234",  
  "type": "KeyVessel",  
  "vesselRef": "urn:mrn:eshuv:portcalls:mastervessel:imo:9863637",  
  "imo": 9863637,  
  "mmsi": 210049000,  
  "callSign": "5BPC3",  
  "flagCode": "ES",  
  "vesselName": "ELEANOR R.",  
  "portCode": "ESHUV",  
  "lastPortCode": "ESPMI",  
  "nextPortCode": "ESVLC",  
  "portCallNumber": "ESHUV202401233",  
  "portCallRef": "urn:mrn:eshuv:portcalls:portcall:code:1233",  
  "dataProvider": "AIS",  
  "latitude": 37.2614,  
  "longitude": -6.9447,  
  "speedOverGround": 11.3,  
  "courseOverGround": 122,  
  "navigationStatus": 4,  
  "observedDate": "2024-07-01T03:11:32Z",  
  "modifiedDate": "2024-07-01T03:07:12Z",  
  "createdDate": "2023-06-03T07:00:00Z",  
  "deletedDate": "2024-07-01T03:07:12Z",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.Ports/master/context.jsonld"  
  ]  
}  
```
</details>
 
#### KeyVessel NGSI-LD 정규화 예제
 
KeyVessel의 JSON-LD 형식의 정규화 예입니다. NGSI-LD와 호환되며 옵션을 사용하지 않고 개별 엔티티의 컨텍스트 데이터를 반환합니다.
<details><summary><strong>예제 보기/숨기기</strong></summary>
 
```json  
{  
  "id": "urn:ngsi-ld:KeyVessel:urn:mrn:eshuv:portcalls:portcallvessel:id:1234",  
  "type": "KeyVessel",  
  "vesselRef": {  
    "type": "Property",  
    "value": "urn:mrn:eshuv:portcalls:mastervessel:imo:9863637"  
  },  
  "imo": {  
    "type": "Property",  
    "value": 9863637  
  },  
  "mmsi": {  
    "type": "Property",  
    "value": 210049000  
  },  
  "callSign": {  
    "type": "Property",  
    "value": "5BPC3"  
  },  
  "flagCode": {  
    "type": "Property",  
    "value": "ES"  
  },  
  "vesselName": {  
    "type": "Property",  
    "value": "ELEANOR R."  
  },  
  "portCode": {  
    "type": "Property",  
    "value": "ESHUV"  
  },  
  "lastPortCode": {  
    "type": "Property",  
    "value": "ESPMI"  
  },  
  "nextPortCode": {  
    "type": "Property",  
    "value": "ESVLC"  
  },  
  "portCallNumber": {  
    "type": "Property",  
    "value": "ESHUV202401233"  
  },  
  "portCallRef": {  
    "type": "Property",  
    "value": "urn:mrn:eshuv:portcalls:portcall:code:1233"  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": "AIS"  
  },  
  "latitude": {  
    "type": "Property",  
    "value": 37.2614  
  },  
  "longitude": {  
    "type": "Property",  
    "value": -6.9447  
  },  
  "speedOverGround": {  
    "type": "Property",  
    "value": 11.3  
  },  
  "courseOverGround": {  
    "type": "Property",  
    "value": 122  
  },  
  "navigationStatus": {  
    "type": "Property",  
    "value": 4  
  },  
  "observedDate": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2024-07-01T03:11:32Z"  
    }  
  },  
  "modifiedDate": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2024-07-01T03:07:12Z"  
    }  
  },  
  "createdDate": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2023-06-03T07:00:00Z"  
    }  
  },  
  "deletedDate": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2024-07-01T03:07:12Z"  
    }  
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