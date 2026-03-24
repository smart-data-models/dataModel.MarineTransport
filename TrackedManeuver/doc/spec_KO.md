<!-- 10-Header -->  
 
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
 
엔티티: TrackedManeuver  
=======================<!-- /10-Header -->  
 
<!-- 15-License -->  
 
[Open License](https://github.com/smart-data-models//dataModel.MarineTransport/blob/master/TrackedManeuver/LICENSE.md)  
 
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
 
<!-- 20-Description -->  
 
전역 설명: **TrackedManoeuvre 엔티티는 Tracked(운항 추적 시스템)에서 가져옵니다. 추적된 조종 동작입니다. 엔티티 ID는 mrn:urn:eshuv:pdph:Tracked:type:attr:value 패턴을 따르며, type=Manoeuvre 및 attr=manoeuvreCode입니다**  
 
버전: 0.0.1  
<!-- /20-Description -->  
 
<!-- 30-PropertiesList -->  
 

## 속성 목록  

 
<sup><sub>[*] 속성에 유형이 없으면 여러 유형이나 다른 형식/패턴을 가질 수 있습니다</sub></sup>  
- `address[object]`: 우편 주소입니다. 모델: [https://schema.org/address](https://schema.org/address)  
	- `addressCountry[string]`: 국가입니다. 예: 스페인입니다. 모델: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: 지역은 거리 주소가 있는 지역이며, 지역은 국가에 있습니다. 모델: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: 지역은 지역이 있는 지역이며, 지역은 국가에 있습니다. 모델: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: 구역은 일부 국가에서 지역 정부가 관리하는 행정 구역 유형입니다  
	- `postOfficeBoxNumber[string]`: 우편함 주소의 우편함 번호입니다. 예: 03578입니다. 모델: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: 우편 번호입니다. 예: 24004입니다. 모델: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: 거리 주소입니다. 모델: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`: 공공 도로의 특정 속성을 식별하는 번호입니다  
- `alternateName[string]`: 이 항목의 대체 이름입니다  
- `amendedOnMooringLocation[string]`: '안정된/변경된 계류' 동작의 위치  
- `anchoringAnchorUpDate[date-time]`:錨 구동(錨 올림) 시간입니다.錨 구동 동작의錨 구동 시간입니다  
- `anchoringDate[date-time]`:錨 내림 시간입니다.錨 구동 동작의錨 내림 시간입니다  
- `anchoringLocation[*]`: 항목에 대한 Geojson 참조입니다. 점, 선, 다각형, 다중 점, 다중 선, 다중 다각형 중 하나일 수 있습니다  
- `anchoringZone[string]`:錨 구동 동작의錨 구동 구역  
- `areaServed[string]`: 서비스 또는 제공 항목이 제공되는 지리적 영역입니다. 모델: [https://schema.org/Text](https://schema.org/Text)  
- `dataProvider[string]`: 조화된 데이터 엔티티를 제공하는 제공자의 일련의 문자입니다  
- `dateCreated[date-time]`: 엔티티 생성 타임스탬프입니다. 보통 저장 플랫폼에서 할당됩니다  
- `dateModified[date-time]`: 엔티티의 마지막 수정 타임스탬프입니다. 보통 저장 플랫폼에서 할당됩니다  
- `description[string]`: 이 항목에 대한 설명입니다  
- `durationHours[number]`: 동작 기간(시간)  
- `endDate[date-time]`: 동작 종료 날짜  
- `id[*]`: 엔티티의 고유 식별자  
- `location[*]`: 항목에 대한 Geojson 참조입니다. 점, 선, 다각형, 다중 점, 다중 선, 다중 다각형 중 하나일 수 있습니다  
- `maneuverCode[string]`: 동작 코드  
- `maneuverType[string]`: 동작 유형  
- `mooringCablesNumber[number]`: 계류 동작의 선 수  
- `mooringChangeCablesNumber[number]`: 계류 변경 동작의 선 수  
- `mooringChangeFirstLandCableDate[date-time]`: 계류 변경 동작의 첫 번째 선 시간  
- `mooringChangeInitialLocation[string]`: 계류 변경 동작의 초기 위치  
- `mooringChangeLastCableDate[date-time]`: 계류 변경 동작의 마지막 선 시간  
- `mooringChangeLastLocation[string]`: 계류 변경 동작의 최종 위치  
- `mooringChangeNoraysFrom[number]`: 계류 변경 동작의 볼라드 번호(부터)  
- `mooringChangeNoraysTo[number]`: 계류 변경 동작의 볼라드 번호(까지)  
- `mooringChangeSide[string]`: 계류 변경 동작의 계류 측  
- `mooringFirstCableDate[date-time]`: 계류 동작의 첫 번째 선 시간  
- `mooringLocation[string]`: 계류 동작의 위치  
- `mooringNoraysFrom[number]`: 계류 동작의 볼라드 번호(부터)  
- `mooringNoraysTo[number]`: 계류 동작의 볼라드 번호(까지)  
- `mooringSide[string]`: 계류 동작의 계류 측  
- `name[string]`: 이 항목의 이름입니다  
- `observations[string]`: 동작 관찰  
- `observedDate[date-time]`: 엔티티의 마지막 업데이트 날짜  
- `othersLocation[*]`: 항목에 대한 Geojson 참조입니다. 점, 선, 다각형, 다중 점, 다중 선, 다중 다각형 중 하나일 수 있습니다  
- `othersType[string]`: 기타 동작 유형  
- `othersZone[string]`: 기타 동작의 구역/위치  
- `owner[array]`: 소유자(들)의 고유 ID를 참조하는 JSON으로 인코딩된 문자열 시퀀스를 포함하는 목록  
- `pilotageDisembarkDate[date-time]`: 조종 동작의 조종자 하선 시간  
- `pilotageDisembarkLocation[string]`: 조종 동작의 조종자 하선 위치  
- `pilotageEmbarkDate[date-time]`: 조종 동작의 조종자 승선 시간  
- `pilotageEmbarkLocation[string]`: 조종 동작의 조종자 승선 위치  
- `pilotageExempt[string]`: 조종 면제  
- `pilotageObservations[string]`: 조종 동작 관찰  
- `pilotagePilots[string]`: 조종 동작에 참여한 조종사  
- `portCallCode[string]`:港口 호출의 STM 등록  
- `refPortCallId[string]`:港口 호출 참조  
- `refTugServiceId[string]`: 견인 서비스 참조  
- `seeAlso[*]`: 항목에 대한 추가 리소스를 가리키는 URI 목록  
- `source[string]`: 엔티티 데이터의 원래 출처를 URL로 제공하는 문자열 시퀀스입니다. 제공자 도메인 이름 또는 원본 객체 URL을 권장합니다  
- `startDate[date-time]`: 동작 시작 날짜  
- `tugboatsNumber[number]`: 견인 서비스 동작의 견인선 수  
- `tugboatsObservations[string]`: 견인 서비스 동작 관찰  
- `type[string]`: NGSI 엔티티 유형입니다. TrackedManoeuvre이어야 합니다  
- `undockingLastCableDate[date-time]`: 계류 해제(계류 해제) 동작의 마지막 선 시간  
- `undockingLocation[string]`: 계류 해제(계류 해제) 동작의 위치  
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
 
알파벳순으로 정렬됨(자세한 정보를 위해 클릭)  
<!-- /50-DataModelHeader -->  
 
<!-- 60-ModelYaml -->  
 
<details><summary><strong>전체 yaml 세부 정보</strong></summary>    
 
```yaml  
TrackedManeuver:    
  description: TrackedManoeuvre entity coming from Tracked (Operation Tracking System). Tracked maneuver. The entityId follows the pattern mrn:urn:eshuv:pdph:Tracked:type:attr:value, where type=Manoeuvre and attr=manoeuvreCode    
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
    amendedOnMooringLocation:    
      description: Location of the 'made fast alongside / amended on mooring' maneuver    
      type: string    
      x-ngsi:    
        type: Property    
    anchoringAnchorUpDate:    
      description: Anchor aweigh (anchor up) time for the anchoring maneuver    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    anchoringDate:    
      description: Anchor down time for the anchoring maneuver    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    anchoringLocation:    
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
    anchoringZone:    
      description: Anchorage zone for the anchoring maneuver    
      type: string    
      x-ngsi:    
        type: Property    
    areaServed:    
      description: The geographic area where a service or offered item is provided    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
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
    description:    
      description: A description of this item    
      type: string    
      x-ngsi:    
        type: Property    
    durationHours:    
      description: Maneuver duration in hours    
      type: number    
      x-ngsi:    
        type: Property    
    endDate:    
      description: Maneuver end date    
      format: date-time    
      type: string    
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
    maneuverCode:    
      description: Maneuver code    
      type: string    
      x-ngsi:    
        type: Property    
    maneuverType:    
      description: Maneuver type    
      type: string    
      x-ngsi:    
        type: Property    
    mooringCablesNumber:    
      description: Number of lines for the mooring maneuver    
      type: number    
      x-ngsi:    
        type: Property    
    mooringChangeCablesNumber:    
      description: Number of lines for the berth-shifting maneuver    
      type: number    
      x-ngsi:    
        type: Property    
    mooringChangeFirstLandCableDate:    
      description: First shore line time for the berth-shifting maneuver    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    mooringChangeInitialLocation:    
      description: Initial location of the berth-shifting maneuver    
      type: string    
      x-ngsi:    
        type: Property    
    mooringChangeLastCableDate:    
      description: Last line time for the berth-shifting maneuver    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    mooringChangeLastLocation:    
      description: Final location of the berth-shifting maneuver    
      type: string    
      x-ngsi:    
        type: Property    
    mooringChangeNoraysFrom:    
      description: Bollard number from (berth-shifting maneuver)    
      type: number    
      x-ngsi:    
        type: Property    
    mooringChangeNoraysTo:    
      description: Bollard number to (berth-shifting maneuver)    
      type: number    
      x-ngsi:    
        type: Property    
    mooringChangeSide:    
      description: Mooring side for the berth-shifting maneuver    
      type: string    
      x-ngsi:    
        type: Property    
    mooringFirstCableDate:    
      description: First line time for the mooring maneuver    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    mooringLocation:    
      description: Location of the mooring maneuver    
      type: string    
      x-ngsi:    
        type: Property    
    mooringNoraysFrom:    
      description: Bollard number from (mooring maneuver)    
      type: number    
      x-ngsi:    
        type: Property    
    mooringNoraysTo:    
      description: Bollard number to (mooring maneuver)    
      type: number    
      x-ngsi:    
        type: Property    
    mooringSide:    
      description: Mooring side for the mooring maneuver    
      type: string    
      x-ngsi:    
        type: Property    
    name:    
      description: The name of this item    
      type: string    
      x-ngsi:    
        type: Property    
    observations:    
      description: Maneuver observations    
      type: string    
      x-ngsi:    
        type: Property    
    observedDate:    
      description: Last update date of the entity    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    othersLocation:    
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
    othersType:    
      description: Type of other maneuver    
      type: string    
      x-ngsi:    
        type: Property    
    othersZone:    
      description: Zone/location of the other maneuver    
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
    pilotageDisembarkDate:    
      description: Pilot disembarkation time for the pilotage maneuver    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    pilotageDisembarkLocation:    
      description: Pilot disembarkation location for the pilotage maneuver    
      type: string    
      x-ngsi:    
        type: Property    
    pilotageEmbarkDate:    
      description: Pilot embarkation time for the pilotage maneuver    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    pilotageEmbarkLocation:    
      description: Pilot embarkation location for the pilotage maneuver    
      type: string    
      x-ngsi:    
        type: Property    
    pilotageExempt:    
      description: Pilotage exemption    
      type: string    
      x-ngsi:    
        type: Property    
    pilotageObservations:    
      description: Pilotage maneuver observations    
      type: string    
      x-ngsi:    
        type: Property    
    pilotagePilots:    
      description: Pilots involved in the pilotage maneuver    
      type: string    
      x-ngsi:    
        type: Property    
    portCallCode:    
      description: STM register of the port call    
      type: string    
      x-ngsi:    
        type: Property    
    refPortCallId:    
      description: Reference to the port call    
      type: string    
      x-ngsi:    
        type: Property    
    refTugServiceId:    
      description: Reference to the tug service    
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
    startDate:    
      description: Maneuver start date    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    tugboatsNumber:    
      description: Number of tugboats for the tug service maneuver    
      type: number    
      x-ngsi:    
        type: Property    
    tugboatsObservations:    
      description: Tug service maneuver observations    
      type: string    
      x-ngsi:    
        type: Property    
    type:    
      description: NGSI Entity type. It has to be TrackedManoeuvre    
      enum:    
        - TrackedManeuver    
      type: string    
      x-ngsi:    
        type: Property    
    undockingLastCableDate:    
      description: Last line time for the unmooring (undocking) maneuver    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    undockingLocation:    
      description: Location of the unmooring (undocking) maneuver    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: ''    
  x-disclaimer: Redistribution and use in source and binary forms...    
  x-license-url: https://github.com/smart-data-models/dataModel.MarineTransport/blob/master/TrackedManeuver/LICENSE.md    
  x-model-schema: https://raw.githubusercontent.com/smart-data-models/dataModel.MarineTransport/master/TrackedManoeuvre/schema.json    
  x-model-tags: ESHUV, i4trust, Tracked    
  x-version: 0.0.1    
```  
</details>    
 
<!-- /60-ModelYaml -->  
 
<!-- 70-MiddleNotes -->  
 
<!-- /70-MiddleNotes -->  
 
<!-- 80-Examples -->  
 
## 예제 페이로드  
 
#### TrackedManeuver NGSI-v2 키-값 예제  
 
TrackedManeuver의 JSON 형식 키-값 예입니다. 이는 `options=keyValues`를 사용하여 개별 엔티티의 컨텍스트 데이터를 반환할 때 NGSI-v2와 호환됩니다.  
<details><summary><strong>예제 표시/숨기기</strong></summary>    
 
```json  
{  
  "id": "mrn:urn:eshuv:pdph:sigo:sigomanoeuvre:manoeuvrecode:E11:22-M2",  
  "type": "TrackedManeuver",  
  "observedDate": "2024-06-14T08:30:00Z",  
  "refPortCallId": "mrn:urn:eshuv:pdph:sigo:sigoportcall:stmregister:E36:24",  
  "refTugServiceId": "mrn:urn:eshuv:pdph:sigo:sigotugboat:name:examplename",  
  "portCallCode": "E36/24",  
  "maneuverCode": "E11/22-M2",  
  "maneuverType": "Atraque",  
  "startDate": "2024-06-14T08:30:00Z",  
  "endDate": "2024-06-14T08:30:00Z",  
  "durationHours": 0.33,  
  "observations": "Observaciones de Maniobra ejemplo",  
  "mooringFirstCableDate": "2024-06-14T08:30:00Z",  
  "mooringLocation": "PANTALAN ERCROSS-ARAGONESAS",  
  "mooringCablesNumber": 3,  
  "mooringNoraysFrom": 4,  
  "mooringNoraysTo": 6,  
  "mooringSide": "Babor",  
  "mooringChangeLastCableDate": "2024-06-14T08:30:00Z",  
  "mooringChangeInitialLocation": "REINA SOFIA",  
  "mooringChangeFirstLandCableDate": "2024-06-14T08:30:00Z",  
  "mooringChangeLastLocation": "MUELLE SUR",  
  "mooringChangeCablesNumber": 2,  
  "mooringChangeNoraysFrom": 1,  
  "mooringChangeNoraysTo": 3,  
  "mooringChangeSide": "string",  
  "undockingLastCableDate": "2024-06-14T08:30:00Z",  
  "undockingLocation": "REINA SOFIA",  
  "amendedOnMooringLocation": "REINA SOFIA",  
  "anchoringZone": "string",  
  "anchoringLocation": {  
    "type": "Point",  
    "coordinates": [-6.3872, 36.02]  
  },  
  "anchoringDate": "2024-06-14T08:30:00Z",  
  "anchoringAnchorUpDate": "2024-06-14T08:30:00Z",  
  "othersType": "string",  
  "othersZone": "string",  
  "othersLocation": {  
    "type": "Point",  
    "coordinates": [-6.3872, 36.02]  
  },  
  "pilotageEmbarkLocation": "LEVANTE NORTE",  
  "pilotageEmbarkDate": "2024-06-14T08:30:00Z",  
  "pilotageDisembarkLocation": "LEVANTE SUR",  
  "pilotageDisembarkDate": "2024-06-14T08:30:00Z",  
  "pilotagePilots": "Carlos Bernal",  
  "pilotageExempt": "No",  
  "pilotageObservations": "Observaciones de practicaje",  
  "tugboatsNumber": 1,  
  "tugboatsObservations": "Observaciones de remolque"  
}  
```  
</details>  
 
#### TrackedManeuver NGSI-v2 정규화 예제  
 
TrackedManeuver의 JSON 형식 정규화 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>예제 표시/숨기기</strong></summary>    
 
```json  
{  
  "id": "mrn:urn:eshuv:pdph:sigo:sigomanoeuvre:manoeuvrecode:E11:22-M2",  
  "type": "TrackedManeuver",  
  "observedDate": {  
    "type": "DateTime",  
    "value": "2024-06-14T08:30:00Z"  
  },  
  "refPortCallId": {  
    "type": "Text",  
    "value": "mrn:urn:eshuv:pdph:sigo:sigoportcall:stmregister:E36:24"  
  },  
  "refTugServiceId": {  
    "type": "Text",  
    "value": "mrn:urn:eshuv:pdph:sigo:sigotugboat:name:examplename"  
  },  
  "portCallCode": {  
    "type": "Text",  
    "value": "E36/24"  
  },  
  "maneuverCode": {  
    "type": "Text",  
    "value": "E11/22-M2"  
  },  
  "maneuverType": {  
    "type": "Text",  
    "value": "Atraque"  
  },  
  "startDate": {  
    "type": "DateTime",  
    "value": "2024-06-14T08:30:00Z"  
  },  
  "endDate": {  
    "type": "DateTime",  
    "value": "2024-06-14T08:30:00Z"  
  },  
  "durationHours": {  
    "type": "Number",  
    "value": 0.33  
  },  
  "observations": {  
    "type": "Text",  
    "value": "Observaciones de Maniobra ejemplo"  
  },  
  "mooringFirstCableDate": {  
    "type": "DateTime",  
    "value": "2024-06-14T08:30:00Z"  
  },  
  "mooringLocation": {  
    "type": "Text",  
    "value": "PANTALAN ERCROSS-ARAGONESAS"  
  },  
  "mooringCablesNumber": {  
    "type": "Number",  
    "value": 3  
  },  
  "mooringNoraysFrom": {  
    "type": "Number",  
    "value": 4  
  },  
  "mooringNoraysTo": {  
    "type": "Number",  
    "value": 6  
  },  
  "mooringSide": {  
    "type": "Text",  
    "value": "Babor"  
  },  
  "mooringChangeLastCableDate": {  
    "type": "DateTime",  
    "value": "2024-06-14T08:30:00Z"  
  },  
  "mooringChangeInitialLocation": {  
    "type": "Text",  
    "value": "REINA SOFIA"  
  },  
  "mooringChangeFirstLandCableDate": {  
    "type": "DateTime",  
    "value": "2024-06-14T08:30:00Z"  
  },  
  "mooringChangeLastLocation": {  
    "type": "Text",  
    "value": "MUELLE SUR"  
  },  
  "mooringChangeCablesNumber": {  
    "type": "Number",  
    "value": 2  
  },  
  "mooringChangeNoraysFrom": {  
    "type": "Number",  
    "value": 1  
  },  
  "mooringChangeNoraysTo": {  
    "type": "Number",  
    "value": 3  
  },  
  "mooringChangeSide": {  
    "type": "Text",  
    "value": "string"  
  },  
  "undockingLastCableDate": {  
    "type": "DateTime",  
    "value": "2024-06-14T08:30:00Z"  
  },  
  "undockingLocation": {  
    "type": "Text",  
    "value": "REINA SOFIA"  
  },  
  "amendedOnMooringLocation": {  
    "type": "Text",  
    "value": "REINA SOFIA"  
  },  
  "anchoringZone": {  
    "type": "Text",  
    "value": "string"  
  },  
  "anchoringLocation": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -6.3872,  
        36.02  
      ]  
    }  
  },  
  "anchoringDate": {  
    "type": "DateTime",  
    "value": "2024-06-14T08:30:00Z"  
  },  
  "anchoringAnchorUpDate": {  
    "type": "DateTime",  
    "value": "2024-06-14T08:30:00Z"  
  },  
  "othersType": {  
    "type": "Text",  
    "value": "string"  
  },  
  "othersZone": {  
    "type": "Text",  
    "value": "string"  
  },  
  "othersLocation": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -6.3872,  
        36.02  
      ]  
    }  
  },  
  "pilotageEmbarkLocation": {  
    "type": "Text",  
    "value": "LEVANTE NORTE"  
  },  
  "pilotageEmbarkDate": {  
    "type": "DateTime",  
    "value": "2024-06-14T08:30:00Z"  
  },  
  "pilotageDisembarkLocation": {  
    "type": "Text",  
    "value": "LEVANTE SUR"  
  },  
  "pilotageDisembarkDate": {  
    "type": "DateTime",  
    "value": "2024-06-14T08:30:00Z"  
  },  
  "pilotagePilots": {  
    "type": "Text",  
    "value": "Carlos Bernal"  
  },  
  "pilotageExempt": {  
    "type": "Text",  
    "value": "No"  
  },  
  "pilotageObservations": {  
    "type": "Text",  
    "value": "Observaciones de practicaje"  
  },  
  "tugboatsNumber": {  
    "type": "Number",  
    "value": 1  
  },  
  "tugboatsObservations": {  
    "type": "Text",  
    "value": "Observaciones de remolque"  
  }  
}  
```  
</details>  
 
#### TrackedManeuver NGSI-LD 키-값 예제  
 
TrackedManeuver의 JSON-LD 형식 키-값 예입니다. 이는 `options=keyValues`를 사용하여 개별 엔티티의 컨텍스트 데이터를 반환할 때 NGSI-LD와 호환됩니다.  
<details><summary><strong>예제 표시/숨기기</strong></summary>    
 
```json  
{  
  "id": "urn:ngsi-ld:TrackedManeuver:mrn:urn:eshuv:pdph:sigo:sigomanoeuvre:manoeuvrecode:E11:22-M2",  
  "type": "TrackedManeuver",  
  "observedDate": "2024-06-14T08:30:00Z",  
  "refPortCallId": "urn:ngsi-ld:PortCallId:mrn:urn:eshuv:pdph:sigo:sigoportcall:stmregister:E36:24",  
  "refTugServiceId": "urn:ngsi-ld:TugServiceId:mrn:urn:eshuv:pdph:sigo:sigotugboat:name:examplename",  
  "portCallCode": "E36/24",  
  "maneuverCode": "E11/22-M2",  
  "maneuverType": "Atraque",  
  "startDate": "2024-06-14T08:30:00Z",  
  "endDate": "2024-06-14T08:30:00Z",  
  "durationHours": 0.33,  
  "observations": "Observaciones de Maniobra ejemplo",  
  "mooringFirstCableDate": "2024-06-14T08:30:00Z",  
  "mooringLocation": "PANTALAN ERCROSS-ARAGONESAS",  
  "mooringCablesNumber": 3,  
  "mooringNoraysFrom": 4,  
  "mooringNoraysTo": 6,  
  "mooringSide": "Babor",  
  "mooringChangeLastCableDate": "2024-06-14T08:30:00Z",  
  "mooringChangeInitialLocation": "REINA SOFIA",  
  "mooringChangeFirstLandCableDate": "2024-06-14T08:30:00Z",  
  "mooringChangeLastLocation": "MUELLE SUR",  
  "mooringChangeCablesNumber": 2,  
  "mooringChangeNoraysFrom": 1,  
  "mooringChangeNoraysTo": 3,  
  "mooringChangeSide": "string",  
  "undockingLastCableDate": "2024-06-14T08:30:00Z",  
  "undockingLocation": "REINA SOFIA",  
  "amendedOnMooringLocation": "REINA SOFIA",  
  "anchoringZone": "string",  
  "anchoringLocation": {  
    "type": "Point",  
    "coordinates": [  
      -6.3872,  
      36.02  
    ]  
  },  
  "anchoringDate": "2024-06-14T08:30:00Z",  
  "anchoringAnchorUpDate": "2024-06-14T08:30:00Z",  
  "othersType": "string",  
  "othersZone": "string",  
  "othersLocation": {  
    "type": "Point",  
    "coordinates": [  
      -6.3872,  
      36.02  
    ]  
  },  
  "pilotageEmbarkLocation": "LEVANTE NORTE",  
  "pilotageEmbarkDate": "2024-06-14T08:30:00Z",  
  "pilotageDisembarkLocation": "LEVANTE SUR",  
  "pilotageDisembarkDate": "2024-06-14T08:30:00Z",  
  "pilotagePilots": "Carlos Bernal",  
  "pilotageExempt": "No",  
  "pilotageObservations": "Observaciones de practicaje",  
  "tugboatsNumber": 1,  
  "tugboatsObservations": "Observaciones de remolque",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.Ports/master/context.jsonld"  
  ]  
}  
```  
</details>  
 
#### TrackedManeuver NGSI-LD 정규화 예제  
 
TrackedManeuver의 JSON-LD 형식 정규화 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>예제 표시/숨기기</strong></summary>    
 
```json  
{  
  "id": "urn:ngsi-ld:TrackedManeuver:mrn:urn:eshuv:pdph:sigo:sigomanoeuvre:manoeuvrecode:E11:22-M2",  
  "type": "TrackedManeuver",  
  "observedDate": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2024-06-14T08:30:00Z"  
    }  
  },  
  "refPortCallId": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:PortCallId:mrn:urn:eshuv:pdph:sigo:sigoportcall:stmregister:E36:24"  
  },  
  "refTugServiceId": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:TugServiceId:mrn:urn:eshuv:pdph:sigo:sigotugboat:name:examplename"  
  },  
  "portCallCode": {  
    "type": "Property",  
    "value": "E36/24"  
  },  
  "maneuverCode": {  
    "type": "Property",  
    "value": "E11/22-M2"  
  },  
  "maneuverType": {  
    "type": "Property",  
    "value": "Atraque"  
  },  
  "startDate": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2024-06-14T08:30:00Z"  
    }  
  },  
  "endDate": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2024-06-14T08:30:00Z"  
    }  
  },  
  "durationHours": {  
    "type": "Property",  
    "value": 0.33  
  },  
  "observations": {  
    "type": "Property",  
    "value": "Observaciones de Maniobra ejemplo"  
  },  
  "mooringFirstCableDate": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2024-06-14T08:30:00Z"  
    }  
  },  
  "mooringLocation": {  
    "type": "Property",  
    "value": "PANTALAN ERCROSS-ARAGONESAS"  
  },  
  "mooringCablesNumber": {  
    "type": "Property",  
    "value": 3  
  },  
  "mooringNoraysFrom": {  
    "type": "Property",  
    "value": 4  
  },  
  "mooringNoraysTo": {  
    "type": "Property",  
    "value": 6  
  },  
  "mooringSide": {  
    "type": "Property",  
    "value": "Babor"  
  },  
  "mooringChangeLastCableDate": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2024-06-14T08:30:00Z"  
    }  
  },  
  "mooringChangeInitialLocation": {  
    "type": "Property",  
    "value": "REINA SOFIA"  
  },  
  "mooringChangeFirstLandCableDate": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2024-06-14T08:30:00Z"  
    }  
  },  
  "mooringChangeLastLocation": {  
    "type": "Property",  
    "value": "MUELLE SUR"  
  },  
  "mooringChangeCablesNumber": {  
    "type": "Property",  
    "value": 2  
  },  
  "mooringChangeNoraysFrom": {  
    "type": "Property",  
    "value": 1  
  },  
  "mooringChangeNoraysTo": {  
    "type": "Property",  
    "value": 3  
  },  
  "mooringChangeSide": {  
    "type": "Property",  
    "value": "string"  
  },  
  "undockingLastCableDate": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2024-06-14T08:30:00Z"  
    }  
  },  
  "undockingLocation": {  
    "type": "Property",  
    "value": "REINA SOFIA"  
  },  
  "amendedOnMooringLocation": {  
    "type": "Property",  
    "value": "REINA SOFIA"  
  },  
  "anchoringZone": {  
    "type": "Property",  
    "value": "string"  
  },  
  "anchoringLocation": {  
    "type": "GeoProperty",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -6.3872,  
        36.02  
      ]  
    }  
  },  
  "anchoringDate": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2024-06-14T08:30:00Z"  
    }  
  },  
  "anchoringAnchorUpDate": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2024-06-14T08:30:00Z"  
    }  
  },  
  "othersType": {  
    "type": "Property",  
    "value": "string"  
  },  
  "othersZone": {  
    "type": "Property",  
    "value": "string"  
  },  
  "othersLocation": {  
    "type": "GeoProperty",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -6.3872,  
        36.02  
      ]  
    }  
  },  
  "pilotageEmbarkLocation": {  
    "type": "Property",  
    "value": "LEVANTE NORTE"  
  },  
  "pilotageEmbarkDate": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2024-06-14T08:30:00Z"  
    }  
  },  
  "pilotageDisembarkLocation": {  
    "type": "Property",  
    "value": "LEVANTE SUR"  
  },  
  "pilotageDisembarkDate": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2024-06-14T08:30:00Z"  
    }  
  },  
  "pilotagePilots": {  
    "type": "Property",  
    "value": "Carlos Bernal"  
  },  
  "pilotageExempt": {  
    "type": "Property",  
    "value": "No"  
  },  
  "pilotageObservations": {  
    "type": "Property",  
    "value": "Observaciones de practicaje"  
  },  
  "tugboatsNumber": {  
    "type": "Property",  
    "value": 1  
  },  
  "tugboatsObservations": {  
    "type": "Property",  
    "value": "Observaciones de remolque"  
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
 
[FAQ 10](https://smartdatamodels.org/index.php/faqs/)를 참조하여 크기 단위에 대한 처리 방법에 대한 답변을 얻으십시오  
<!-- /95-Units -->  
 
<!-- 97-LastFooter -->  
 
---  
 
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
 
