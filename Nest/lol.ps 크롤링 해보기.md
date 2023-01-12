

## lol.ps 크롤링 해보기

![Untitled](https://user-images.githubusercontent.com/65094518/212028745-d301e786-65a7-4315-a06b-6ae7ef34e454.png)

테그로 정보를 주지 않고 svelte? 로 정보 테그가 바뀌었습니다. script 태그 안에 모든 정보가 들어가있고 html에서 정보를 조합하는 형태같습니다.



### script 테그 가져오는법

```tsx
const $ = cheerio.load(html);
          const scriptContents = $('script')
            .map((i, el) => $(el).html())
            .get();
```

[lol.ps](http://lol.ps) 홈페이지에 html테그 안에는 5개의 script 태그가 있습니다. 그중에 내가 원하는 데이터가 들어가있는 테그는 5번째 script 테그 입니다.

map으로 각 태그를 돌면서 태그안에 객체를 가져옵니다.

```jsx
[null,{"type":"data","data":{"user":null},"uses":{}},null,{"type":"data","data":{"versionInfo":[{"versionId":63,"description":"13.1","patchDate":"2023-01-10","isActive":true,"createdAt":"2023-01-10T23:20:26.351Z","updatedAt":"2023-01-10T23:20:26.351Z"},{"versionId":62,"description":"12.23b","patchDate":"2022-12-14","isActive":true,"createdAt":"2023-01-10T18:50:07.012Z","updatedAt":"2023-01-10T18:50:07.012Z"},{"versionId":61,"description":"12.23","patchDate":"2022-12-07","isActive":true,"createdAt":"2023-01-10T18:50:07.012Z","updatedAt":"2023-01-10T18:50:07.012Z"}],"championArguments":{"regionId":0,"tierId":2,"championId":1,"versionId":63,"laneId":2},"champSummary":[{"id":"496981","buildTypeId":0,"winRate":"53.35","pickRate":"0.53","banRate":"0.03","lastPsScore":"47.55","psScore":"43.92","lastRanking":46,"ranking":50,"top1LaneId":2,"top1LaneRatio":"82.65","top2LaneId":4,"top2LaneRatio":"15.90","top3LaneId":0,"top3LaneRatio":"1.20","counterChampionIdList":[55,91,101,3,157],"counterWinrateList":[28.57,33.33,33.33,33.33,36.36],"counterCountList":[14,6,6,6,11],"counterEasyChampionIdList":[34,112,4,7,103],"counterEasyWinrateList":[85.71,75,71.43,66.67,64.29],"counterEasyCountList":[7,8,7,12,14],"mainRuneCategory":8100,"subRuneCategory":8200,"mainRune1":8112,"mainRune2":8126,"mainRune3":8138,"mainRune4":8105,"subRune1":8226,"subRune2":8233,"statperk1Id":5008,"statperk2Id":5008,"statperk3Id":5003,"spell1Id":4,"spell2Id":14,"skillMasterList":["Q","W","E"],"startingItemIdList":[[1056],[2003,2003]],"coreItemIdList":[6655,4645,3157],"skillLv15List":["Q","W","E","Q","Q","R","Q","W","Q","W","R","W","W","E","E"],"shoesId":3020,"item_1coreList":[6655,3152,6653],"item_2coreList":[4645,3157,3165],"item_3coreList":[3157,3135,3089],"createdAt":"2023-01-12T02:57:43.122Z","updatedAt":"2023-01-12T02:57:43.000Z","buildWinRate":null,"buildPickRate":null,"count":343,"buildCount":null,"psTier":5,"item_4coreList":[],"item_5coreList":[],"runeTotalWinrate":"49.46","runeTotalPickrate":"34.83","runeTotalCount":93,"skillMasterWinrate":"64.79","skillMasterPickrate":"85.54","skillMasterCount":71,"startingWinrate":"53.07","startingPickrate":"95.37","startingCount":309,"top1ThreeCoreIdList":[6655,4645,3157],"top1ThreeCorePickrate":"35.90","top1ThreeCoreWinrate":"57.14","top1ThreeCoreCount":14,"top2ThreeCoreIdList":[6655,4645,3135],"top2ThreeCorePickrate":"17.95","top2ThreeCoreWinrate":"57.14","top2ThreeCoreCount":7,"top3ThreeCoreIdList":[6655,4645,3089],"top3ThreeCorePickrate":"15.38","top3ThreeCoreWinrate":"83.33","top3ThreeCoreCount":6,"top4LaneId":3,"top4LaneRatio":"0.24","top5LaneId":1,"top5LaneRatio":"0.00","championId":1,"laneId":2,"regionId":0,"tierId":2,"versionId":63,"top3_1stCoreIdList":[6655,3152,6653],"top3_2ndCoreIdList":[4645,3157,3165],"top3_3rdCoreIdList":[3157,3135,3089],"top3_1stCoreWinrateList":[51.3,41.18,30.77],"top3_2ndCoreWinrateList":[60.32,62.5,57.14],"top3_3rdCoreWinrateList":[60,69.23,83.33],"top3_1stCorePickrateList":[83.7,9.24,7.07],"top3_2ndCorePickrateList":[57.8,29.36,12.84],"top3_3rdCorePickrateList":[51.28,33.33,15.38],"top3_1stCoreCountList":[154,17,13],"top3_2ndCoreCountList":[63,32,14],"top3_3rdCoreCountList":[20,13,6],"isOp":false,"isHoney":false},{"id":"496982","buildTypeId":1,"winRate":"53.35","pickRate":"0.53","banRate":"0.03","lastPsScore":"47.55","psScore":"43.92","lastRanking":46,"ranking":50,"top1LaneId":2,"top1LaneRatio":"82.65","top2LaneId":4,"top2LaneRatio":"15.90","top3LaneId":0,"top3LaneRatio":"1.20","counterChampionIdList":[55,91,101,3,157],"counterWinrateList":[28.57,33.33,33.33,33.33,36.36],"counterCountList":[14,6,6,6,11],"counterEasyChampionIdList":[34,112,4,7,103],"counterEasyWinrateList":[85.71,75,71.43,66.67,64.29],"counterEasyCountList":[7,8,7,12,14],"mainRuneCategory":8100,"subRuneCategory":8200,"mainRune1":8112,"mainRune2":8139,"mainRune3":8138,"mainRune4":8105,"subRune1":8226,"subRune2":8233,"statperk1Id":5008,"statperk2Id":5008,"statperk3Id":5002,"spell1Id":4,"spell2Id":14,"skillMasterList":["Q","W","E"],"startingItemIdList":[[1056],[2003,2003]],"coreItemIdList":[6655,4645,3157],"skillLv15List":["Q","W","E","Q","Q","R","W","W","W","W","R","Q","Q","E","E"],"shoesId":3020,"item_1coreList":[6655,3152,6653],"item_2coreList":[3157,4645,3165],"item_3coreList":[3089,3135,3157],"createdAt":"2023-01-12T02:57:43.122Z","updatedAt":"2023-01-12T02:57:43.000Z","buildWinRate":null,"buildPickRate":null,"count":343,"buildCount":null,"psTier":5,"item_4coreList":[],"item_5coreList":[],"runeTotalWinrate":"72.09","runeTotalPickrate":"16.10","runeTotalCount":43,"skillMasterWinrate":"64.79","skillMasterPickrate":"85.54","skillMasterCount":71,"startingWinrate":"53.07","startingPickrate":"95.37","startingCount":309,"top1ThreeCoreIdList":[6655,4645,3089],"top1ThreeCorePickrate":"15.38","top1ThreeCoreWinrate":"83.33","top1ThreeCoreCount":6,"top2ThreeCoreIdList":[6655,3157,3135],"top2ThreeCorePickrate":"15.38","top2ThreeCoreWinrate":"83.33","top2ThreeCoreCount":6,"top3ThreeCoreIdList":[6655,3165,3157],"top3ThreeCorePickrate":"15.38","top3ThreeCoreWinrate":"66.67","top3ThreeCoreCount":6,"top4LaneId":3,"top4LaneRatio":"0.24","top5LaneId":1,"top5LaneRatio":"0.00","championId":1,"laneId":2,"regionId":0,"tierId":2,"versionId":63,"top3_1stCoreIdList":[6655,3152,6653],"top3_2ndCoreIdList":[3157,4645,3165],"top3_3rdCoreIdList":[3089,3135,3157],"top3_1stCoreWinrateList":[51.3,41.18,30.77],"top3_2ndCoreWinrateList":[62.5,60.32,57.14],"top3_3rdCoreWinrateList":[83.33,69.23,60],"top3_1stCorePickrateList":[83.7,9.24,7.07],"top3_2ndCorePickrateList":[29.36,57.8,12.84],"top3_3rdCorePickrateList":[15.38,33.33,51.28],"top3_1stCoreCountList":[154,17,13],"top3_2ndCoreCountList":[32,63,14],"top3_3rdCoreCountList":[6,13,20],"isOp":false,"isHoney":false}]},"uses":{"params":["id"]}}]
```

그러면 위 같은 못생긴 코드들이 나오게 됩니다.

JSON.parse로 json형태로 만들어주면

```jsx
const scriptContentObject = JSON.parse(scriptContents[5]);
[
  null,
  { type: 'data', data: { user: null }, uses: {} },
  null,
  {
    type: 'data',
    data: {
      versionInfo: [Array],
      championArguments: [Object],
      champSummary: [Array]
    },
    uses: { params: [Array] }
  }
]
```

이런식으로 구성되있다는것을 알 수 있습니다.

string[] 으로 되어있고 그안에 또 객체들을 가지고 있습니다.

이중에 data 객체를 뽑아보면

```jsx
const scriptContentObjectInData = scriptContentObject[3] as Record<string,any>;
console.log(scriptContentObjectInData.data);
{
  versionInfo: [
    {
      versionId: 63,
      description: '13.1',
      patchDate: '2023-01-10',
      isActive: true,
      createdAt: '2023-01-10T23:20:26.351Z',
      updatedAt: '2023-01-10T23:20:26.351Z'
    },
    {
      versionId: 62,
      description: '12.23b',
      patchDate: '2022-12-14',
      isActive: true,
      createdAt: '2023-01-10T18:50:07.012Z',
      updatedAt: '2023-01-10T18:50:07.012Z'
    },
    {
      versionId: 61,
      description: '12.23',
      patchDate: '2022-12-07',
      isActive: true,
      createdAt: '2023-01-10T18:50:07.012Z',
      updatedAt: '2023-01-10T18:50:07.012Z'
    }
  ],
  championArguments: { regionId: 0, tierId: 2, championId: 1, versionId: 63, laneId: 2 },
  champSummary: [
    {
      id: '496981',
      buildTypeId: 0,
      winRate: '53.35',
      pickRate: '0.53',
      banRate: '0.03',
      lastPsScore: '47.55',
      psScore: '43.92',
      lastRanking: 46,
      ranking: 50,
      top1LaneId: 2,
      top1LaneRatio: '82.65',
      top2LaneId: 4,
      top2LaneRatio: '15.90',
      top3LaneId: 0,
      top3LaneRatio: '1.20',
      counterChampionIdList: [Array],
      counterWinrateList: [Array],
      counterCountList: [Array],
      counterEasyChampionIdList: [Array],
      counterEasyWinrateList: [Array],
      counterEasyCountList: [Array],
      mainRuneCategory: 8100,
      subRuneCategory: 8200,
      mainRune1: 8112,
      mainRune2: 8126,
      mainRune3: 8138,
      mainRune4: 8105,
      subRune1: 8226,
      subRune2: 8233,
      statperk1Id: 5008,
      statperk2Id: 5008,
      statperk3Id: 5003,
      spell1Id: 4,
      spell2Id: 14,
      skillMasterList: [Array],
      startingItemIdList: [Array],
      coreItemIdList: [Array],
      skillLv15List: [Array],
      shoesId: 3020,
      item_1coreList: [Array],
      item_2coreList: [Array],
      item_3coreList: [Array],
      createdAt: '2023-01-12T02:57:43.122Z',
      updatedAt: '2023-01-12T02:57:43.000Z',
      buildWinRate: null,
      buildPickRate: null,
      count: 343,
      buildCount: null,
      psTier: 5,
      item_4coreList: [],
      item_5coreList: [],
      runeTotalWinrate: '49.46',
      runeTotalPickrate: '34.83',
      runeTotalCount: 93,
      skillMasterWinrate: '64.79',
      skillMasterPickrate: '85.54',
      skillMasterCount: 71,
      startingWinrate: '53.07',
      startingPickrate: '95.37',
      startingCount: 309,
      top1ThreeCoreIdList: [Array],
      top1ThreeCorePickrate: '35.90',
      top1ThreeCoreWinrate: '57.14',
      top1ThreeCoreCount: 14,
      top2ThreeCoreIdList: [Array],
      top2ThreeCorePickrate: '17.95',
      top2ThreeCoreWinrate: '57.14',
      top2ThreeCoreCount: 7,
      top3ThreeCoreIdList: [Array],
      top3ThreeCorePickrate: '15.38',
      top3ThreeCoreWinrate: '83.33',
      top3ThreeCoreCount: 6,
      top4LaneId: 3,
      top4LaneRatio: '0.24',
      top5LaneId: 1,
      top5LaneRatio: '0.00',
      championId: 1,
      laneId: 2,
      regionId: 0,
      tierId: 2,
      versionId: 63,
      top3_1stCoreIdList: [Array],
      top3_2ndCoreIdList: [Array],
      top3_3rdCoreIdList: [Array],
      top3_1stCoreWinrateList: [Array],
      top3_2ndCoreWinrateList: [Array],
      top3_3rdCoreWinrateList: [Array],
      top3_1stCorePickrateList: [Array],
      top3_2ndCorePickrateList: [Array],
      top3_3rdCorePickrateList: [Array],
      top3_1stCoreCountList: [Array],
      top3_2ndCoreCountList: [Array],
      top3_3rdCoreCountList: [Array],
      isOp: false,
      isHoney: false
    },
    {
      id: '496982',
      buildTypeId: 1,
      winRate: '53.35',
      pickRate: '0.53',
      banRate: '0.03',
      lastPsScore: '47.55',
      psScore: '43.92',
      lastRanking: 46,
      ranking: 50,
      top1LaneId: 2,
      top1LaneRatio: '82.65',
      top2LaneId: 4,
      top2LaneRatio: '15.90',
      top3LaneId: 0,
      top3LaneRatio: '1.20',
      counterChampionIdList: [Array],
      counterWinrateList: [Array],
      counterCountList: [Array],
      counterEasyChampionIdList: [Array],
      counterEasyWinrateList: [Array],
      counterEasyCountList: [Array],
      mainRuneCategory: 8100,
      subRuneCategory: 8200,
      mainRune1: 8112,
      mainRune2: 8139,
      mainRune3: 8138,
      mainRune4: 8105,
      subRune1: 8226,
      subRune2: 8233,
      statperk1Id: 5008,
      statperk2Id: 5008,
      statperk3Id: 5002,
      spell1Id: 4,
      spell2Id: 14,
      skillMasterList: [Array],
      startingItemIdList: [Array],
      coreItemIdList: [Array],
      skillLv15List: [Array],
      shoesId: 3020,
      item_1coreList: [Array],
      item_2coreList: [Array],
      item_3coreList: [Array],
      createdAt: '2023-01-12T02:57:43.122Z',
      updatedAt: '2023-01-12T02:57:43.000Z',
      buildWinRate: null,
      buildPickRate: null,
      count: 343,
      buildCount: null,
      psTier: 5,
      item_4coreList: [],
      item_5coreList: [],
      runeTotalWinrate: '72.09',
      runeTotalPickrate: '16.10',
      runeTotalCount: 43,
      skillMasterWinrate: '64.79',
      skillMasterPickrate: '85.54',
      skillMasterCount: 71,
      startingWinrate: '53.07',
      startingPickrate: '95.37',
      startingCount: 309,
      top1ThreeCoreIdList: [Array],
      top1ThreeCorePickrate: '15.38',
      top1ThreeCoreWinrate: '83.33',
      top1ThreeCoreCount: 6,
      top2ThreeCoreIdList: [Array],
      top2ThreeCorePickrate: '15.38',
      top2ThreeCoreWinrate: '83.33',
      top2ThreeCoreCount: 6,
      top3ThreeCoreIdList: [Array],
      top3ThreeCorePickrate: '15.38',
      top3ThreeCoreWinrate: '66.67',
      top3ThreeCoreCount: 6,
      top4LaneId: 3,
      top4LaneRatio: '0.24',
      top5LaneId: 1,
      top5LaneRatio: '0.00',
      championId: 1,
      laneId: 2,
      regionId: 0,
      tierId: 2,
      versionId: 63,
      top3_1stCoreIdList: [Array],
      top3_2ndCoreIdList: [Array],
      top3_3rdCoreIdList: [Array],
      top3_1stCoreWinrateList: [Array],
      top3_2ndCoreWinrateList: [Array],
      top3_3rdCoreWinrateList: [Array],
      top3_1stCorePickrateList: [Array],
      top3_2ndCorePickrateList: [Array],
      top3_3rdCorePickrateList: [Array],
      top3_1stCoreCountList: [Array],
      top3_2ndCoreCountList: [Array],
      top3_3rdCoreCountList: [Array],
      isOp: false,
      isHoney: false
    }
  ]
}
```

이렇게 거대한 객체를 받을 수 있습니다.

우리가 필요한건 champSummary배열 안에있는

```
  counterChampionIdList: [Array],
  counterWinrateList: [Array],
  counterEasyChampionIdList: [Array],
  counterEasyWinrateList: [Array],
```

위 4가지 입니다.

### 그럼 크롤링한 데이터를 해체해야 합니다.

전체적인 형태는 아래와 같습니다.

```jsx
scriptContentObject
 ->[ ... , **data** , ...]
			->{ ..., ..., **champSummary** ]
						-> [ ...champSummaryData ] 		
```

### 코드

```tsx
// 1. lol.ps 챔피언 별로 가지고 오기
const getHtml = async (championNumber: number) => {
  try {
    const result = await axios.get(`https://lol.ps/champ/${championNumber}`, {
      headers: { "Accept-Encoding": "gzip,deflate,compress" }
    });
    return result.data;
  } catch (err) {
    return new Promise((resolve, reject) => {
      reject(err);
    });
  }
};

const html = await getHtml(key);

// 2. 챔피언별 어려운상대, 쉬운상대 3개 뽑기
const $ = cheerio.load(html);
const scriptContents = $("script")
  .map((i, el) => $(el).html())
  .get();
```

1. html을 가져옵니다. 이 때 header에 encoding 방식을 넣어줘야 합니다. 안그러면 에러가 납니다.
2. cheerio로 html 파일을 스캔합니다.
3. html 파일중에 script 테그가 있는것들을 map에다 돌려서 배열 형태로 만들어줍니다.

```tsx
const scriptContentObject = JSON.parse(scriptContents[5]);
const scriptContentObjectInData = scriptContentObject[3] as Record<string, any>;
const scriptCoreDataObject: scriptContentObjectInData = scriptContentObjectInData.data;
```

1. scriptContents는 배열이 됩니다. console.log를 찍어보면 여러개의 배열이 들어있는것을 확인할 수 있습니다. 여기서 저희는 `champSummary` 가 들어있는 5번째 배열에서 Object를 가져옵니다.

2. Object에서도  `champSummary` 를 찾아야 합니다. 3번째에 있으니 다시한번 풉니다.

3. `champSummary`는 data안에 감싸져있으니 감싼 것도 풀어야 합니다.

   **scriptCoreDataObject**의 타입인 **scriptContentObjectInData** 타입 입니다.

   ```
   export interface versionInfoData {
     versionId: number;
     description: string;
     patchDate: string;
     isActive: true;
     createdAt: string;
     updatedAt: string;
   }
   
   export interface champSummaryData {
     id: string;
     buildTypeId: number;
     winRate: string;
     pickRate: string;
     banRate: string;
     lastPsScore: string;
     psScore: string;
     lastRanking: number;
     ranking: number;
     top1LaneId: number;
     top1LaneRatio: string;
     top2LaneId: number;
     top2LaneRatio: string;
     top3LaneId: number;
     top3LaneRatio: string;
     counterChampionIdList: Array<number>;
     counterWinrateList: Array<number>;
     counterCountList: Array<number>;
     counterEasyChampionIdList: Array<number>;
     counterEasyWinrateList: Array<number>;
     counterEasyCountList: Array<number>;
     mainRuneCategory: number;
     subRuneCategory: number;
     mainRune1: number;
     mainRune2: number;
     mainRune3: number;
     mainRune4: number;
     subRune1: number;
     subRune2: number;
     statperk1Id: number;
     statperk2Id: number;
     statperk3Id: number;
     spell1Id: number;
     spell2Id: number;
     skillMasterList: Array<number>;
     startingItemIdList: Array<number>;
     coreItemIdList: Array<number>;
     skillLv15List: Array<string>;
     shoesId: number;
     item_1coreList: Array<number>;
     item_2coreList: Array<number>;
     item_3coreList: Array<number>;
     item_4coreList: Array<number>;
     item_5coreList: Array<number>;
     createdAt: string;
     updatedAt: string;
     buildWinRate: null;
     buildPickRate: null;
     count: number;
     buildCount: null;
     psTier: number;
     runeTotalWinrate: string;
     runeTotalPickrate: string;
     runeTotalCount: number;
     skillMasterWinrate: string;
     skillMasterPickrate: string;
     skillMasterCount: number;
     startingWinrate: string;
     startingPickrate: string;
     startingCount: number;
     top1ThreeCoreIdList: Array<number>;
     top1ThreeCorePickrate: string;
     top1ThreeCoreWinrate: string;
     top1ThreeCoreCount: number;
     top2ThreeCoreIdList: Array<number>;
     top2ThreeCorePickrate: string;
     top2ThreeCoreWinrate: string;
     top2ThreeCoreCount: number;
     top3ThreeCoreIdList: Array<number>;
     top3ThreeCorePickrate: string;
     top3ThreeCoreWinrate: string;
     top3ThreeCoreCount: number;
     top4LaneId: number;
     top4LaneRatio: string;
     top5LaneId: number;
     top5LaneRatio: string;
     championId: number;
     laneId: number;
     regionId: number;
     tierId: number;
     versionId: number;
     top3_1stCoreIdList: Array<number>;
     top3_2ndCoreIdList: Array<number>;
     top3_3rdCoreIdList: Array<number>;
     top3_1stCoreWinrateList: Array<number>;
     top3_2ndCoreWinrateList: Array<number>;
     top3_3rdCoreWinrateList: Array<number>;
     top3_1stCorePickrateList: Array<number>;
     top3_2ndCorePickrateList: Array<number>;
     top3_3rdCorePickrateList: Array<number>;
     top3_1stCoreCountList: Array<number>;
     top3_2ndCoreCountList: Array<number>;
     top3_3rdCoreCountList: Array<number>;
     isOp: false;
     isHoney: false;
   }
   
   export interface scriptContentObjectInData {
     versionInfo: Array<versionInfoData>;
     championArguments: {
       regionId: number;
       tierId: number;
       championId: number;
       versionId: number;
       laneId: number;
     };
     champSummary: Array<champSummaryData>;
   }
   ```

```tsx
// 챔피언의 능력치가 모두 들어가있는 코어 객체
const ChampionSummaryObject: champSummaryData = scriptCoreDataObject.champSummary[0];
```

이제 `champSummary`를 찾았습니다. 이걸로 데이터를 조작하면 됩니다.