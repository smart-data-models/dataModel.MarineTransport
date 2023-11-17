<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
엔티티: 선박    
=======<!-- /10-Header -->    
<!-- 15-License -->    
[오픈 라이선스](https://github.com/smart-data-models//dataModel.MarineTransport/blob/master/Vessel/LICENSE.md)    
[문서 자동 생성](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
글로벌 설명: **데이터 모델은 선박에 대한 정보를 제공하기 위한 것입니다. 각 선박의 속성(정적 및 동적 정보**)을 나타낼 수 있습니다.    
버전: 0.0.2    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## 속성 목록    
<sup><sub>[*] 속성에 유형이 없는 것은 여러 유형 또는 다른 형식/패턴을 가질 수 있기 때문입니다</sub></sup>.    
- `address[object]`: 우편 주소  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: 국가. 예를 들어, 스페인  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)    
	- `addressLocality[string]`: 도로명 주소가 있는 지역 및 해당 지역에 속한 지역  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)    
	- `addressRegion[string]`: 해당 지역이 위치한 지역과 해당 국가의 지역  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)    
	- `district[string]`: 지구는 일부 국가에서는 지방 정부에서 관리하는 행정 구역의 일종입니다.      
	- `postOfficeBoxNumber[string]`: 사서함 주소의 우체국 사서함 번호입니다. 예: 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)    
	- `postalCode[string]`: 우편 번호입니다. 예: 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)    
	- `streetAddress[string]`: 거리 주소  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)    
	- `streetNr[string]`: 공공 도로의 특정 건물을 식별하는 번호      
- `airDraught[number]`: 공기 흘수(선박의 가장 높은 지점에서 수면선까지의 거리)  . Model: [http://schema.org/Number](http://schema.org/Number)- `alternateName[string]`: 이 항목의 대체 이름  - `areaServed[string]`: 서비스 또는 제공 품목이 제공되는 지리적 영역  . Model: [https://schema.org/Text](https://schema.org/Text)- `beam[number]`: 선박의 빔  . Model: [https://schema.org/Number](https://schema.org/Number)- `buildingAt[date-time]`: ISO 8601 UTC 형식으로 표시되는 선박 건조 날짜 및 시간  . Model: [https://schema.org/Text](https://schema.org/Text)- `callSign[string]`: 해상 호출 부호는 선박에 고유 식별자로 할당된 호출 부호입니다.  . Model: [https://schema.org/Text](https://schema.org/Text)- `courseOverGround[number]`: 코스 오버 그라운드(COG)  . Model: [https://schema.org/Number](https://schema.org/Number)- `createdAt[date-time]`: ISO 8601 UTC 형식으로 표시되는 엔티티 생성 날짜 및 시간  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: 조화된 데이터 엔티티의 공급자를 식별하는 일련의 문자  . Model: [https://schema.org/Text](https://schema.org/Text)- `dateCreated[date-time]`: 엔티티 생성 타임스탬프. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `dateModified[date-time]`: 엔티티의 마지막 수정 타임스탬프입니다. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `deadweightTonnage[number]`: 재화중량톤수(DWT)  . Model: [https://schema.org/Number](https://schema.org/Number)- `description[string]`: 이 항목에 대한 설명  - `destinationPort[string]`: 목적지 항구(지리적 코딩 체계 UN/LOCODE(국제연합 무역 및 운송 위치 코드). https://unece.org/trade/publications/recommendation-ndeg16-united-nations-code-trade-and-transport-locations)  . Model: [https://schema.org/Text](https://schema.org/Text)- `draught[number]`: 흘수(수면과 선체 바닥(용골) 사이의 수직 거리)  . Model: [http://schema.org/Number](http://schema.org/Number)- `estimatedTimeOfArrival[date-time]`: 배송업체가 원래 계획하고 입력한 도착 예정 시간(ISO 8601 UTC 형식으로 표시됨)  . Model: [https://schema.org/Text](https://schema.org/Text)- `financialOwner[string]`: 재무 소유자  . Model: [https://schema.org/Text](https://schema.org/Text)- `flagCode[string]`: 국제 깃발 코드(ISO 3166-1 알파-2)  . Model: [https://schema.org/Text](https://schema.org/Text)- `grossTonnage[number]`: 총 톤수(GT)  . Model: [https://schema.org/Number](https://schema.org/Number)- `heading[number]`: 선박의 방향(HDG)  . Model: [https://schema.org/Number](https://schema.org/Number)- `id[string]`: 엔티티의 고유 식별자  - `imo[number]`: 국제 해사기구 번호(글로벌 영구 UID)  . Model: [https://schema.org/Number](https://schema.org/Number)- `length[number]`: 선박 길이  . Model: [https://schema.org/Number](https://schema.org/Number)- `location[object]`: 항목에 대한 지오슨 참조입니다. 포인트, 라인스트링, 폴리곤, 멀티포인트, 멀티라인스트링 또는 멀티폴리고프로퍼티일 수 있습니다.  	- `coordinates`:       
	- `type`:       
- `manager[string]`: 관리자 선박  . Model: [https://schema.org/Text](https://schema.org/Text)- `maximumDraught[number]`: 최대 통풍  . Model: [https://schema.org/Number](https://schema.org/Number)- `mmsi[number]`: 해양 모바일 서비스 식별 번호(해당 개체의 현재 플래그 상태에 의해 발급된 임시로 할당된 UID)  . Model: [https://schema.org/Number](https://schema.org/Number)- `modifiedAt[date-time]`: ISO 8601 UTC 형식으로 표시되는 엔티티의 마지막 수정 날짜 및 시간  . Model: [https://schema.org/Text](https://schema.org/Text)- `name[string]`: 선박 이름  . Model: [https://schema.org/Text](https://schema.org/Text)- `navigationStatus[number]`: Enum: '0=엔진 사용 중,1=정박 중,2=지휘권 없음,3=기동성 제한,4=흘수의 제약,5=정박 중,6=육상,7=어업 중,8=항해 중,9=향후 HSC 항해 상태 변경을 위해 유보됨,10=향후 WIG 항법 상태 수정 유보,11=향후 사용 유보,12=향후 사용 유보,13=향후 사용 유보,14=AIS-SART 활성화됨,15=정의되지 않음(기본값)'. 내비게이션 상태. AIVDM/AIVDO 데이터 형식  . Model: [http://schema.org/Number](http://schema.org/Number)- `observedAt[date-time]`: 이 관측의 날짜 및 시간은 ISO 8601 UTC 형식으로 표시됩니다.  . Model: [https://schema.org/Text](https://schema.org/Text)- `owner[array]`: 소유자의 고유 ID를 참조하는 JSON 인코딩된 문자 시퀀스가 포함된 목록입니다.  - `ownerVessel[string]`: 소유자 선박  . Model: [https://schema.org/Text](https://schema.org/Text)- `photo[string]`: 선박 사진 URL  . Model: [https://schema.org/Text](https://schema.org/Text)- `positionAccuracy[number]`: 글로벌 항법 위성 시스템(GNSS) 수신기 또는 기타 전자식 위치 고정 장치, 기본값),1=높음(10m 미만, 차동 모드(예: DGNSS 수신기)'. 선박 위치 플래그의 정확도 코드  . Model: [https://schema.org/Number.Enum: 0=Low (> 10 m; autonomous mode of e.g](https://schema.org/Number.Enum: 0=Low (> 10 m; autonomous mode of e.g)- `previousPort[string]`: 이전 항구(지리적 코딩 체계 UN/LOCODE(국제연합 무역 및 운송 위치 코드). https://unece.org/trade/publications/recommendation-ndeg16-united-nations-code-trade-and-transport-locations)  . Model: [https://schema.org/Text](https://schema.org/Text)- `rateOfTurn[number]`: 회전율(ROT)  . Model: [https://schema.org/Number](https://schema.org/Number)- `seeAlso[*]`: 항목에 대한 추가 리소스를 가리키는 URL 목록  - `source[string]`: 엔티티 데이터의 원본 소스를 URL로 제공하는 문자 시퀀스입니다. 소스 공급자의 정규화된 도메인 이름 또는 소스 개체에 대한 URL을 사용하는 것이 좋습니다.  - `specialManeuverIndicator[number]`: Enum: '0=사용 불가(기본값), 1=특수 기동 중이 아님, 2=특수 기동 중'. 특수 기동 플래그 코드  . Model: [https://schema.org/Number](https://schema.org/Number)- `speedOverGround[number]`: 지상 속도(SOG)  . Model: [https://schema.org/Number](https://schema.org/Number)- `technicalManager[string]`: 기술 관리자  . Model: [https://schema.org/Text](https://schema.org/Text)- `toBow[number]`: 활의 치수  . Model: [http://schema.org/Number](http://schema.org/Number)- `toPort[number]`: 포트 치수  . Model: [http://schema.org/Number](http://schema.org/Number)- `toStardboard[number]`: 우현 치수  . Model: [http://schema.org/Number](http://schema.org/Number)- `toStern[number]`: 선미까지의 치수  . Model: [http://schema.org/Number](http://schema.org/Number)- `type[string]`: NGSI 엔티티 유형. Vessel이어야 합니다.  - `vesselSubType[number]`: Enum: '0=사용 불가(기본값),1-19=향후 사용을 위해 예약됨,20=지상익기(WIG), 이 유형의 모든 선박,21=지상익기(WIG), 위험 범주 A,22=지상익기(WIG), 위험 범주 B,23=지상익선(WIG), 위험 범주 C,24=지상익선(WIG), 위험 범주 D,25-29=지상익선(WIG), 향후 사용 예약,30=어업,31=예인,32=예인: 길이 200m 초과 또는 폭 25m 초과,33=준설 또는 수중 작업,34=잠수 작업,35=군용 작업,36=항해,37=유람선,38-39=유보,40=고속선(HSC), 모든 유형의 선박,41=고속선(HSC), 위험 범주 A,42=고속선(HSC), 위험 범주 B,43=고속선(HSC), 위험 범주 C,44=고속선박(HSC), 위험 범주 D,45-48=고속선박(HSC), 향후 사용 예약,49=고속선박(HSC), 추가 정보 없음,50=도선선,51=수색 및 구조선,52=예인선,53=항만 예인선,54=오염 방지 장비,55=법 집행선,56-57=스페어 - 지역 선박,58=의료 수송선,59=RR 결의안에 따른 비 전투용 선박 번호. 18,60=여객, 이 유형의 모든 선박,61=여객, 위험 범주 A,62=여객, 위험 범주 B,63=여객, 위험 범주 C,64=여객, 위험 범주 D,65-68=여객, 향후 사용을 위해 예약,69=여객, 추가 정보 없음,70=화물, 이 유형의 모든 선박,71=화물, 위험 범주 A,72=화물, 위험 범주 B,73=화물, 위험 범주 C,74=화물, 위험 범주 D,75-78=화물, 향후 사용을 위해 예약,79=화물, 추가 정보 없음,80=탱커, 이 유형의 모든 선박,81=유조선, 위험 범주 A,82=유조선, 위험 범주 B,83=유조선, 위험 범주 C,84=유조선, 위험 범주 D,85-88=유조선, 향후 사용을 위해 예약,89=유조선, 추가 정보 없음,90=기타 유형, 이 유형의 모든 선박,91=기타 유형, 위험 범주 A,92=기타 유형, 위험 범주 B,93=기타 유형, 위험 범주 C,94=기타 유형, 위험 범주 D,95-98=기타 유형, 향후 사용을 위해 예약,99=기타 유형, 추가 정보 없음'. 선박 하위 유형 코드  . Model: [https://schema.org/Number](https://schema.org/Number)- `vesselType[number]`: 열거형: '1=예약,2=지상익,3=특수 범주,4=고속선박,5=특수 범주,6=여객,7=화물,8=탱커,9=기타'. 선박 유형 코드  . Model: [https://schema.org/Number](https://schema.org/Number)<!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
필수 속성    
- `id`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## 속성에 대한 데이터 모델 설명    
알파벳순으로 정렬(자세한 내용을 보려면 클릭)    
<!-- /50-DataModelHeader -->    
<!-- 60-ModelYaml -->    
<details><summary><strong>full yaml details</strong></summary>      
```yaml    
Vessel:      
  description: 'The data model is intended to provide information about vessels. It allows to represent the properties of each vessel: static and dynamic information'      
  properties:      
    address:      
      description: The mailing address      
      properties:      
        addressCountry:      
          description: 'The country. For example, Spain'      
          type: string      
          x-ngsi:      
            model: https://schema.org/addressCountry      
            type: Property      
        addressLocality:      
          description: 'The locality in which the street address is, and which is in the region'      
          type: string      
          x-ngsi:      
            model: https://schema.org/addressLocality      
            type: Property      
        addressRegion:      
          description: 'The region in which the locality is, and which is in the country'      
          type: string      
          x-ngsi:      
            model: https://schema.org/addressRegion      
            type: Property      
        district:      
          description: 'A district is a type of administrative division that, in some countries, is managed by the local government'      
          type: string      
          x-ngsi:      
            type: Property      
        postOfficeBoxNumber:      
          description: 'The post office box number for PO box addresses. For example, 03578'      
          type: string      
          x-ngsi:      
            model: https://schema.org/postOfficeBoxNumber      
            type: Property      
        postalCode:      
          description: 'The postal code. For example, 24004'      
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
    airDraught:      
      description: Air Draught (distance from the top of a vessel''s highest point to its waterline)      
      type: number      
      x-ngsi:      
        model: http://schema.org/Number      
        type: Property      
        units: ' meters'      
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
    beam:      
      description: Beam of Vessel      
      maximum: 1000      
      minimum: 0      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
        units: ' meters'      
    buildingAt:      
      description: Date and time of building of the vessel represented by an ISO 8601 UTC format      
      format: date-time      
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
        units: ' degree'      
    createdAt:      
      description: Date and time of creation of the entity represented by an ISO 8601 UTC format      
      format: date-time      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    dataProvider:      
      description: A sequence of characters identifying the provider of the harmonised data entity      
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
    deadweightTonnage:      
      description: Deadweight Tonnage (DWT)      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
        units: ' tons'      
    description:      
      description: A description of this item      
      type: string      
      x-ngsi:      
        type: Property      
    destinationPort:      
      description: 'Destination Port (Geographic coding scheme UN/LOCODE (United Nations Code for Trade and Transport Locations). https://unece.org/trade/publications/recommendation-ndeg16-united-nations-code-trade-and-transport-locations)'      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    draught:      
      description: Draught (vertical distance between the waterline and the bottom of the hull (keel))      
      type: number      
      x-ngsi:      
        model: http://schema.org/Number      
        type: Property      
        units: ' meters'      
    estimatedTimeOfArrival:      
      description: 'Estimated time of arrival, as it was originally planned and entered by the shipper, represented by an ISO 8601 UTC format'      
      format: date-time      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    financialOwner:      
      description: Financial Owner      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    flagCode:      
      description: International Flag Code (ISO 3166-1 alfa-2)      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    grossTonnage:      
      description: Gross Tonnage (GT)      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
        units: ' moorson tons'      
    heading:      
      description: Heading of the Vessel (HDG)      
      maximum: 511      
      minimum: 0      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
        units: ' degree'      
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
        type: Property      
    imo:      
      description: International Maritime Organization Number (a global forever UID)      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
    length:      
      description: Length of Vessel      
      maximum: 8000      
      minimum: 0      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
        units: ' meters'      
    location:      
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'      
      oneOf:      
        - description: Geojson reference to the item. Point      
          properties:      
            bbox:      
              items:      
                type: number      
              minItems: 4      
              type: array      
            coordinates:      
              items:      
                type: number      
              minItems: 2      
              type: array      
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
              items:      
                type: number      
              minItems: 4      
              type: array      
            coordinates:      
              items:      
                items:      
                  type: number      
                minItems: 2      
                type: array      
              minItems: 2      
              type: array      
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
              items:      
                type: number      
              minItems: 4      
              type: array      
            coordinates:      
              items:      
                items:      
                  items:      
                    type: number      
                  minItems: 2      
                  type: array      
                minItems: 4      
                type: array      
              type: array      
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
              items:      
                type: number      
              minItems: 4      
              type: array      
            coordinates:      
              items:      
                items:      
                  type: number      
                minItems: 2      
                type: array      
              type: array      
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
              items:      
                type: number      
              minItems: 4      
              type: array      
            coordinates:      
              items:      
                items:      
                  items:      
                    type: number      
                  minItems: 2      
                  type: array      
                minItems: 2      
                type: array      
              type: array      
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
    manager:      
      description: Manager Vessel      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    maximumDraught:      
      description: Maximum Draught      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
        units: ' meters'      
    mmsi:      
      description: 'Marine Mobile Service Identity Number (a temporarily assigned UID, issued by that object''s current flag state)'      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
    modifiedAt:      
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
      description: 'Enum: ''0=Under way using engine,1=At anchor,2=Not under command,3=Restricted manoeuverability,4=Constrained by her draught,5=Moored,6=Aground,7=Engaged in Fishing,8=Under way sailing,9=Reserved for future amendment of Navigational Status for HSC,10=Reserved for future amendment of Navigational Status for WIG,11=Reserved for future use,12=Reserved for future use,13=Reserved for future use,14=AIS-SART is active,15=Not defined (default)''. Navigation Status. AIVDM/AIVDO data format'      
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
        model: http://schema.org/Number      
        type: Property      
    observedAt:      
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
          type: Property      
      type: array      
      x-ngsi:      
        type: Property      
    ownerVessel:      
      description: Owner Vessel      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    photo:      
      description: Vessel Photo URL      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    positionAccuracy:      
      description: 'global navigation satellite system (GNSS) receiver or of other electronic position fixing device; default),1=High (< 10 m; differential mode of e.g. DGNSS receiver)''. Code for the accuracy of the vessel position flag'      
      enum:      
        - 0      
        - 1      
      type: number      
      x-ngsi:      
        model: 'https://schema.org/Number.Enum: 0=Low (> 10 m; autonomous mode of e.g'      
        type: Property      
    previousPort:      
      description: 'Previous Port (Geographic coding scheme UN/LOCODE (United Nations Code for Trade and Transport Locations). https://unece.org/trade/publications/recommendation-ndeg16-united-nations-code-trade-and-transport-locations)'      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    rateOfTurn:      
      description: Rate of Turn (ROT)      
      maximum: 708      
      minimum: 0      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
        units: ' degree'      
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
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'      
      type: string      
      x-ngsi:      
        type: Property      
    specialManeuverIndicator:      
      description: 'Enum: ''0=Not available (default),1=Not engaged in special maneuver,2=Engaged in special maneuver''. Code for the special maneuver flag'      
      enum:      
        - 0      
        - 1      
        - 2      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
    speedOverGround:      
      description: Speed Over Ground (SOG)      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
        units: ' meters per second'      
    technicalManager:      
      description: Technical Manager      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    toBow:      
      description: Dimension to Bow      
      type: number      
      x-ngsi:      
        model: http://schema.org/Number      
        type: Property      
        units: ' meters'      
    toPort:      
      description: Dimension to Port      
      type: number      
      x-ngsi:      
        model: http://schema.org/Number      
        type: Property      
        units: ' meters'      
    toStardboard:      
      description: Dimension to Starboard      
      type: number      
      x-ngsi:      
        model: http://schema.org/Number      
        type: Property      
        units: ' meters'      
    toStern:      
      description: Dimension to Stern      
      type: number      
      x-ngsi:      
        model: http://schema.org/Number      
        type: Property      
        units: ' meters'      
    type:      
      description: NGSI Entity type. It has to be Vessel      
      enum:      
        - Vessel      
      type: string      
      x-ngsi:      
        type: Property      
    vesselSubType:      
      description: 'Enum: ''0=Not available (default),1-19=Reserved for future use,20=Wing in ground (WIG), all ships of this type,21=Wing in ground (WIG), Hazardous category A,22=Wing in ground (WIG), Hazardous category B,23=Wing in ground (WIG), Hazardous category C,24=Wing in ground (WIG), Hazardous category D,25-29=Wing in ground (WIG), Reserved for future use,30=Fishing,31=Towing,32=Towing: length exceeds 200m or breadth exceeds 25m,33=Dredging or underwater ops,34=Diving ops,35=Military ops,36=Sailing,37=Pleasure Craft,38-39=Reserved,40=High speed craft (HSC), all ships of this type,41=High speed craft (HSC), Hazardous category A,42=High speed craft (HSC), Hazardous category B,43=High speed craft (HSC), Hazardous category C,44=High speed craft (HSC), Hazardous category D,45-48=High speed craft (HSC), Reserved for future use,49=High speed craft (HSC), No additional information,50=Pilot Vessel,51=Search and Rescue vessel,52=Tug,53=Port Tender,54=Anti-pollution equipment,55=Law Enforcement,56-57=Spare - Local Vessel,58=Medical Transport,59=Noncombatant ship according to RR Resolution No. 18,60=Passenger, all ships of this type,61=Passenger, Hazardous category A,62=Passenger, Hazardous category B,63=Passenger, Hazardous category C,64=Passenger, Hazardous category D,65-68=Passenger, Reserved for future use,69=Passenger, No additional information,70=Cargo, all ships of this type,71=Cargo, Hazardous category A,72=Cargo, Hazardous category B,73=Cargo, Hazardous category C,74=Cargo, Hazardous category D,75-78=Cargo, Reserved for future use,79=Cargo, No additional information,80=Tanker, all ships of this type,81=Tanker, Hazardous category A,82=Tanker, Hazardous category B,83=Tanker, Hazardous category C,84=Tanker, Hazardous category D,85-88=Tanker, Reserved for future use,89=Tanker, No additional information,90=Other Type, all ships of this type,91=Other Type, Hazardous category A,92=Other Type, Hazardous category B,93=Other Type, Hazardous category C,94=Other Type, Hazardous category D,95-98=Other Type, Reserved for future use,99=Other Type, no additional information''. Code for vessel Sub-Type'      
      enum:      
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
        - 16      
        - 17      
        - 18      
        - 19      
        - 20      
        - 21      
        - 22      
        - 23      
        - 24      
        - 25      
        - 26      
        - 27      
        - 28      
        - 29      
        - 30      
        - 31      
        - 32      
        - 33      
        - 34      
        - 35      
        - 36      
        - 37      
        - 38      
        - 39      
        - 40      
        - 41      
        - 42      
        - 43      
        - 44      
        - 45      
        - 46      
        - 47      
        - 48      
        - 49      
        - 50      
        - 51      
        - 52      
        - 53      
        - 54      
        - 55      
        - 56      
        - 57      
        - 58      
        - 59      
        - 60      
        - 61      
        - 62      
        - 63      
        - 64      
        - 65      
        - 66      
        - 67      
        - 68      
        - 69      
        - 70      
        - 71      
        - 72      
        - 73      
        - 74      
        - 75      
        - 76      
        - 77      
        - 78      
        - 79      
        - 80      
        - 81      
        - 82      
        - 83      
        - 84      
        - 85      
        - 86      
        - 87      
        - 88      
        - 89      
        - 90      
        - 91      
        - 92      
        - 93      
        - 94      
        - 95      
        - 96      
        - 97      
        - 98      
        - 99      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
    vesselType:      
      description: 'Enum: ''1=Reserved,2=Wing In Ground,3=Special Category,4=High-Speed Craft,5=Special Category,6=Passenger,7=Cargo,8=Tanker,9=Other''. Code for vessel type'      
      enum:      
        - 1      
        - 2      
        - 3      
        - 4      
        - 5      
        - 6      
        - 7      
        - 8      
        - 9      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
  required:      
    - id      
    - type      
  type: object      
  x-derived-from: ""      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2023 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.MarineTransport/blob/master/Vessel/LICENSE.md      
  x-model-schema: https://raw.githubusercontent.com/smart-data-models/dataModel.MarineTransport/master/Vessel/schema.json      
  x-model-tags: I4Trust      
  x-version: 0.1.1      
```    
</details>      
<!-- /60-ModelYaml -->    
<!-- 70-MiddleNotes -->    
<!-- /70-MiddleNotes -->    
<!-- 80-Examples -->    
## 페이로드 예시    
#### Vessel NGSI-v2 키-값 예시    
다음은 키-값으로 JSON-LD 형식의 선박 예시입니다. 이는 `옵션=키값`을 사용할 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:mrn:amura:vessel:test",  
  "type": "Vessel",  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      -5.993307,  
      37.362882  
    ]  
  },  
  "imo": 9863637,  
  "mmsi": 210049000,  
  "callSign": "5BPC5",  
  "name": "ELEANOR ROOSEVELT",  
  "speedOverGround": 1,  
  "courseOverGround": 1,  
  "heading": 1,  
  "rateOfTurn": 1,  
  "createdAt": "2022-06-01T07:00:00.00Z",  
  "modifiedAt": "2022-06-01T07:00:00.00Z",  
  "observedAt": "2022-06-01T07:00:00.00Z",  
  "flagCode": "CY",  
  "vesselType": 1,  
  "vesselSubType": 2,  
  "grossTonnage": 12467,  
  "beam": 7,  
  "length": 32,  
  "maximumDraught": 5,  
  "deadweightTonnage": 8,  
  "buildingAt": "2021-01-01T07:00:00.00Z",  
  "toBow": 3,  
  "toStern": 20,  
  "toPort": 17,  
  "toStardboard": 4,  
  "navigationStatus": 4,  
  "airDraught": 4,  
  "draught": 4,  
  "photo": "PHOTO URL",  
  "ownerVessel": "OWNER NAME",  
  "manager": "MANAGER NAME",  
  "financialOwner": "FINANCIAL OWNER NAME",  
  "technicalManager": "TECHNICAL MANAGER NAME",  
  "dataProvider": "AIS",  
  "destinationPort": "ESVLC",  
  "previousPort": "ESPMI",  
  "estimatedTimeOfArrival": "2023-03-01T07:00:00.00Z",  
  "calculatedTimeOfArrival": "2023-03-02T07:00:00.00Z",  
  "positionAccuracy": 0,  
  "specialManeuverIndicator": 1  
}  
```  
</details>    
#### Vessel NGSI-v2 정규화 예제    
다음은 정규화된 JSON-LD 형식의 선박 예시입니다. 이는 옵션을 사용하지 않을 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:mrn:amura:vessel:test",  
  "type": "Vessel",  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -5.993307,  
        37.362882  
      ]  
    }  
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
    "value": "5BPC5"  
  },  
  "name": {  
    "type": "Text",  
    "value": "ELEANOR ROOSEVELT"  
  },  
  "speedOverGround": {  
    "type": "Boolean",  
    "value": true  
  },  
  "courseOverGround": {  
    "type": "Boolean",  
    "value": true  
  },  
  "heading": {  
    "type": "Boolean",  
    "value": true  
  },  
  "rateOfTurn": {  
    "type": "Boolean",  
    "value": true  
  },  
  "createdAt": {  
    "type": "DateTime",  
    "value": "2022-06-01T07:00:00.00Z"  
  },  
  "modifiedAt": {  
    "type": "DateTime",  
    "value": "2022-06-01T07:00:00.00Z"  
  },  
  "observedAt": {  
    "type": "DateTime",  
    "value": "2022-06-01T07:00:00.00Z"  
  },  
  "flagCode": {  
    "type": "Text",  
    "value": "CY"  
  },  
  "vesselType": {  
    "type": "Boolean",  
    "value": true  
  },  
  "vesselSubType": {  
    "type": "Number",  
    "value": 2  
  },  
  "grossTonnage": {  
    "type": "Number",  
    "value": 12467  
  },  
  "beam": {  
    "type": "Number",  
    "value": 7  
  },  
  "length": {  
    "type": "Number",  
    "value": 32  
  },  
  "maximumDraught": {  
    "type": "Number",  
    "value": 5  
  },  
  "deadweightTonnage": {  
    "type": "Number",  
    "value": 8  
  },  
  "buildingAt": {  
    "type": "DateTime",  
    "value": "2021-01-01T07:00:00.00Z1"  
  },  
  "toBow": {  
    "type": "Number",  
    "value": 3  
  },  
  "toStern": {  
    "type": "Number",  
    "value": 20  
  },  
  "toPort": {  
    "type": "Number",  
    "value": 17  
  },  
  "toStardboard": {  
    "type": "Number",  
    "value": 4  
  },  
  "navigationStatus": {  
    "type": "Number",  
    "value": 4  
  },  
  "airDraught": {  
    "type": "Number",  
    "value": 4  
  },  
  "draught": {  
    "type": "Number",  
    "value": 4  
  },  
  "photo": {  
    "type": "Text",  
    "value": "URL PHOTO"  
  },  
  "ownerVessel": {  
    "type": "Text",  
    "value": "OWNER NAME"  
  },  
  "manager": {  
    "type": "Text",  
    "value": "MANAGER NAME"  
  },  
  "financialOwner": {  
    "type": "Text",  
    "value": "FINANCIAL OWNER NAME"  
  },  
  "technicalManager": {  
    "type": "Text",  
    "value": "TECHNICAL MANAGER NAME"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "AIS"  
  },  
  "destinationPort": {  
    "type": "Text",  
    "value": "ESVLC"  
  },  
  "previousPort": {  
    "type": "Text",  
    "value": "ESPMI"  
  },  
  "estimatedTimeOfArrival": {  
    "type": "DateTime",  
    "value": "2023-03-01T07:00:00.00Z"  
  },  
  "positionAccuracy": {  
    "type": "Boolean",  
    "value": false  
  },  
  "specialManeuverIndicator": {  
    "type": "Boolean",  
    "value": true  
  }  
}  
```  
</details>    
#### Vessel NGSI-LD 키-값 예시    
다음은 키-값으로 JSON-LD 형식의 선박 예시입니다. 이는 `옵션=키값`을 사용할 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:mrn:amura:vessel:test",  
  "type": "Vessel",  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      -5.993307,  
      37.362882  
    ]  
  },  
  "imo": 9863637,  
  "mmsi": 210049000,  
  "callSign": "5BPC5",  
  "name": "ELEANOR ROOSEVELT",  
  "speedOverGround": 1,  
  "courseOverGround": 1,  
  "heading": 1,  
  "rateOfTurn": 1,  
  "createdAt": "2022-06-01T07:00:00.00Z",  
  "modifiedAt": "2022-06-01T07:00:00.00Z",  
  "observedAt": "2022-06-01T07:00:00.00Z",  
  "flagCode": "CY",  
  "vesselType": 1,  
  "vesselSubType": 2,  
  "grossTonnage": 12467,  
  "beam": 7,  
  "length": 32,  
  "maximumDraught": 5,  
  "deadweightTonnage": 8,  
  "buildingAt": "2021-01-01T07:00:00.00Z",  
  "toBow": 3,  
  "toStern": 20,  
  "toPort": 17,  
  "toStardboard": 4,  
  "navigationStatus": 4,  
  "airDraught": 4,  
  "draught": 4,  
  "photo": "PHOTO URL",  
  "ownerVessel": "OWNER NAME",  
  "manager": "MANAGER NAME",  
  "financialOwner": "FINANCIAL OWNER NAME",  
  "technicalManager": "TECHNICAL MANAGER NAME",  
  "dataProvider": "AIS",  
  "destinationPort": "ESVLC",  
  "previousPort": "ESPMI",  
  "estimatedTimeOfArrival": "2023-03-01T07:00:00.00Z",  
  "positionAccuracy": 0,  
  "specialManeuverIndicator": 1,  
  "@context": [  
    "https://gitlab.com/hiades/fiware/smart-data-models/-/raw/main/context.jsonld",  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.MarineTransport/master/context.jsonld"  
  ]  
}  
```  
</details>    
#### Vessel NGSI-LD 정규화 예제    
다음은 정규화된 JSON-LD 형식의 선박 예시입니다. 이는 옵션을 사용하지 않을 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
    "id": "urn:mrn:amura:vessel:test",  
    "type": "Vessel",  
    "location": {  
        "type": "GeoProperty",  
        "value": {  
            "type": "Point",  
            "coordinates": [  
                -5.993307,  
                37.362882  
            ]  
        }  
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
        "value": "5BPC5"  
    },  
    "name": {  
        "type": "Property",  
        "value": "ELEANOR ROOSEVELT"  
    },  
    "speedOverGround": {  
        "type": "Property",  
        "value": 1  
    },  
    "courseOverGround": {  
        "type": "Property",  
        "value": 1  
    },  
    "heading": {  
        "type": "Property",  
        "value": 1  
    },  
    "rateOfTurn": {  
        "type": "Property",  
        "value": 1  
    },  
    "createdAt": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2022-06-01T07:00:00.00Z"  
        }  
    },  
    "modifiedAt": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2022-06-01T07:00:00.00Z"  
        }  
    },  
    "observedAt": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2022-06-01T07:00:00.00Z"  
        }  
    },  
    "flagCode": {  
        "type": "Property",  
        "value": "CY"  
    },  
    "vesselType": {  
        "type": "Property",  
        "value": 1  
    },  
    "vesselSubType": {  
        "type": "Property",  
        "value": 2  
    },  
    "grossTonnage": {  
        "type": "Property",  
        "value": 12467  
    },  
    "beam": {  
        "type": "Property",  
        "value": 7  
    },  
    "length": {  
        "type": "Property",  
        "value": 32  
    },  
    "maximumDraught": {  
        "type": "Property",  
        "value": 5  
    },  
    "deadweightTonnage": {  
        "type": "Property",  
        "value": 8  
    },  
    "buildingAt": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2021-01-01T07:00:00.00Z1"  
        }  
    },  
    "toBow": {  
        "type": "Property",  
        "value": 3  
    },  
    "toStern": {  
        "type": "Property",  
        "value": 20  
    },  
    "toPort": {  
        "type": "Property",  
        "value": 17  
    },  
    "toStardboard": {  
        "type": "Property",  
        "value": 4  
    },  
    "navigationStatus": {  
        "type": "Property",  
        "value": 4  
    },  
    "airDraught": {  
        "type": "Property",  
        "value": 4  
    },  
    "draught": {  
        "type": "Property",  
        "value": 4  
    },  
    "photo": {  
        "type": "Property",  
        "value": "URL PHOTO"  
    },  
    "ownerVessel": {  
        "type": "Property",  
        "value": "OWNER NAME"  
    },  
    "manager": {  
        "type": "Property",  
        "value": "MANAGER NAME"  
    },  
    "financialOwner": {  
        "type": "Property",  
        "value": "FINANCIAL OWNER NAME"  
    },  
    "technicalManager": {  
        "type": "Property",  
        "value": "TECHNICAL MANAGER NAME"  
    },  
    "dataProvider": {  
        "type": "Property",  
        "value": "AIS"  
    },  
    "destinationPort": {  
        "type": "Property",  
        "value": "ESVLC"  
    },  
    "previousPort": {  
        "type": "Property",  
        "value": "ESPMI"  
    },  
    "estimatedTimeOfArrival": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2023-03-01T07:00:00.00Z"  
        }  
    },  
    "positionAccuracy": {  
        "type": "Property",  
        "value": 0  
    },  
    "specialManeuverIndicator": {  
        "type": "Property",  
        "value": 1  
    },  
    "@context": [  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.MarineTransport/master/context.jsonld"  
    ]  
}  
```  
</details><!-- /80-Examples -->    
<!-- 90-FooterNotes -->    
<!-- /90-FooterNotes -->    
<!-- 95-Units -->    
10](https://smartdatamodels.org/index.php/faqs/)를 참조하여 규모 단위를 다루는 방법에 대한 답변을 확인하세요.    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
