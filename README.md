# IDO Boğaz Hattı Projesi Optimal İskele Koordinatlarının Belirlenmesi
## Sunuş / Introduction
Gebze Teknik Üniversitesi Bilgisayar Mühendisliği Bölümünde CSE 521 Algoritma Analizi dersi kapsamında verilen IDO Boğaz hattı iskelesi koordinatları için optimal çözümleri bulma projesi kapsamında beş farklı (hırslı sezgisel, dinamik programlama, parçala çöz, kaba kuvvet, dallan sınırla) yöntem kullanılarak problemin çözülmesi ve yöntemlerin farklı büyüklükteki veri setleri ile teorik ve pratik çalışma zamanı sonuçları analiz edilmiştir.

## Problem Tanımı/Problem Definition
IDO İstanbul boğazının Avrupa yakasına Beşiktaş’tan başlamak üzere kuzeye doğru bir dizi iskele kurmak istemektedir. Yaptığı araştırma sonucunda n farklı olası yer tespit etmiştir. Bu olası yerlerin Beşiktaş’a uzaklığı (artan sırada) m 1 , m 2 ,......, m n şeklindedir. Her bir konum için olası yolcu bilgileri analiz edilerek bir yıllık olası kazançlar p 1 , p 2 ,...,p n şeklinde hesaplanmıştır. Çok yakın yerlere iskele kurmamak adına, K belirli bir sayı olmak üzere, her iki iskele arasındaki mesafe en az K kadar olmak zorundadır.

Bu veriler ve kısıtlar altında beklenen IDO’nun bu proje kapsamında elde edebileceği kazancın en az fazla olacağı iskele konumlarının bulunmasıdır.

## Çözüm Yöntemleri / Solution Techniques

Tanımlanan problem için problem çözümlerinde sık şekilde kullanılan beş adet (**hırslı sezgisel, dinamik programlama, parçala çöz, kaba kuvvet, dallan sınırla**) çözüm yöntemini kullanarak optimal çözümü oluşturacak algoritmalar oluşturulmuştur.
Oluşturulan algoritmalar ve bu algoritmalara ait sözde kodlar ile çalışma zamanı analizleri raporda belirtilmiştir.
Çalışmamız kapsamında oluşturduğumuz algoritmalar için girdi olarak aşağıda Tabloda açıklanan değişkenler kullanılmış olup, algoritmaların çıktıları maksimum kazanç bilgisi ve bu kazancı sağlayacak iskele lokasyonlarını içerir listedir.

| Değişken        | Tip         | Açıklama  |
| ------------- |:-------------:| :----- |
| distanceList[1...n] | Dizi | Problem tanımında açıklanan, iskelelerin Beşiktaş’a uzaklıklarını içerir sıralı liste|
| profitList[1...n] | Dizi | İskeleler için yıllık olası kazanç listesi|
| limit | Integer| Problem tanımında K olarak tanımlanan, seçilecek iskeler arasındaki en küçük mesafe |
| rootStationIndex | Integer | Başlangıç iskelesinin listeler içerisindeki indeksi |

#### Çözüm için Kullanılan Algoritmalar
* Hırslı Sezgisel (Greedy)
* Dinamik Programlama (Dynamic Programming)
* Parçala Çöz (Divide and Conqure)
* Kaba Kuvvet (Brute Force)
* Dallan Sınırla (Branch and Bound)

## Deneysel Analiz / 
Geliştirilen algoritmaların çalışma zamanları Tablo 2’de gösterildiği gibidir.

| Algoritma | Çalışma Zamanı | Girdi Boyutu  |
| ------------- |:-------------:| :----- |
| Hırslı Sezgisel | θ(nlogn) | N|
| Dinamik Programlam | O(n^2 ) | N|
| Parça Çöz | Uygulanabilir değil| - |
| Kaba Kuvvet | 2^n | N |
| Dalla Sınırla |  | N |

## Sonuçlar / Conclusion
CSE 521 Algoritma analizi dersi kapsamında IDO İstanbul şehir hatları tarafından Beşiktaş’tan başlamak üzere boğaz kurulmak istenen iskelelerin en çok kazanç sağlayacak iskele lokasyon listenin bulunması amaçlı optimizasyon problemi için beş adet çözüm yöntemi için algoritma geliştirilmiştir. Bu çözüm yöntemleri hırslı sezgisel, dinamik programlama, parçala çöz, kaba kuvvet ve dallan sınırla yöntemleridir. 

Bu yöntemler içerisinde hırslı sezgisel algoritma her zaman optimal çözümü vermemektedir. Bununla birlikte büyük boyutlu veri setleri için hızlı çalışmaktadır. 

Parçala çöz yöntemi için problemi çözebilecek uygun bir algoritma geliştirilememiştir. Bunun nedeni problemin problemin boyutunu küçültecek alt problemlere ayırılamaması olmuştır. Bununla birlikte parçala azalt (divide and decrease) algoritması bu problemin çözümünde uygulanmıştır. 

Kaba kuvvet algoritması küçük boyutlu veri setlerinde sonucu hızlı bir şekilde verebilirken problem boyutu büyüdükçe çalışma zamanı üstsel şekilde arttığından, problem boyutundaki küçük artışlar çalışma zamanında büyük değişimlere neden olmuştur. 

Buna karşı dallan sınırla algoritmasıyla kaba kuvvet algoritmasındaki gereksiz hesaplamalar azaltılarak problemin çalışma zamanı
azaltılmıştır. 

Dinamik programla yöntemi ile de problemin çözümü için fazladan depolama alanları kullanılarak problemin çalışma zamanı belirgin ölçüde azaltılmıştır. 

Tüm bunları sıra problemde kısıtlarından birisi olan iki iskele arasında olabilecek en küçük uzaklığı tanımlayan K değişkenin değeri de problemin çalışma zamanına önemli ölçüde etki ettiği gözlenmiştir. K değerinin küçülmesi problem için çalışma kümesi arttırmakta büyümesi azaltmakta olduğu gözlenmiştir. Problemin çözümüne ilişkin ilgili geliştirilen algoritmalar python programlama dili ortamında uygulanmıştır.

Dinamik programlama, kaba kuvvet, ve dallan sınırla yöntemleri ile problemin çözümü için optimum sonucu verecek algoritmalar oluşturulmuştur.
