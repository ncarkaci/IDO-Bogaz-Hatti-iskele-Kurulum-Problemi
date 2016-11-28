# IDO Boğaz Hattı Projesi Optimal İskele Koordinatlarının Belirlenmesi
1. Sunuş / Introduction
CSE 521 Algoritma Analizi dersi kapsamında verilen IDO Boğaz hattı iskelesi koordinatları için optimal çözümleri verecek beş farklı çözüm yöntemi ile (hırslı sezgisel, dinamik programlama, parçala çöz, kaba kuvvet, dallan sınırla) algoritmaları geliştirilmiş olup, bu algoritmaların uygulaması yapılarak farklı büyüklükteki veri setleri ile teorik ve pratik çalışma zamanı sonuçları analiz edilmiştir.

2. Problem Tanımı/Problem Definition
IDO İstanbul boğazının Avrupa yakasına Beşiktaş’tan başlamak üzere kuzeye doğru bir dizi iskele kurmak istemektedir. Yaptığı araştırma sonucunda n farklı olası yer tespit etmiştir. Bu olası yerlerin Beşiktaş’a uzaklığı (artan sırada) m 1 , m 2 ,......, m n şeklindedir. Her bir konum için olası yolcu bilgileri analiz edilerek bir yıllık olası kazançlar p 1 , p 2 ,...,p n şeklinde hesaplanmıştır. Çok yakın yerlere iskele kurmamak adına, K belirli bir sayı olmak üzere, her iki iskele arasındaki mesafe en az K kadar olmak zorundadır.

Bu veriler ve kısıtlar altında beklenen IDO’nun bu proje kapsamında elde edebileceği kazancın en az fazla olacağı iskele konumlarının bulunmasıdır.

3. Çözüm Yöntemleri / Solution Techniques

Tanımlanan problem için problem çözümlerinde sık şekilde kullanılan beş adet (hırslı sezgisel, dinamik programlama, parçala çöz, kaba kuvvet, dallan sınırla) çözüm yöntemini kullanarak optimal çözümü oluşturacak algoritmalar oluşturulmuştur.
Oluşturulan algoritmalar ve bu algoritmalara ait sözde kodlar ile çalışma zamanı analizleri aşağıdaki gibidir.
Çalışmamız kapsamında oluşturduğumuz algoritmalar için girdi olarak Tablo 1’de açıklanan değişkenler kullanılmış olup, algoritmaların çıktıları maksimum kazanç bilgisi ve bu kazancı sağlayacak iskele lokasyonlarını içerir listedir.
