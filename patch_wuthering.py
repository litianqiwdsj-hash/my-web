import re

with open('E:/web/web.html', 'r', encoding='utf-8') as f:
    content = f.read()

# --- 1. 在 news-grid 里，Niko 卡片之前插入鸣潮x雷蛇卡片 ---
old_cards = """                <!-- Article: Niko Bilibili Live Stream -->
                <div class="news-card" data-news="news_niko">"""

new_wuthering_card = """                <!-- Article: Wuthering Waves x Razer Denia Collaboration -->
                <div class="news-card" data-news="news_wuthering">
                    <div class="news-card-header" style="position:relative;">
                        <!-- ★ 图片替换位置：把下面 src 中的占位图路径换成实际新闻图片路径即可 ★ -->
                        <img src="https://picsum.photos/600/300?random=wuthering_razer" alt="Wuthering x Razer" style="width:100%;height:160px;object-fit:cover;border-radius:14px 14px 0 0;display:block;">
                        <div class="news-meta" style="position:absolute;bottom:10px;left:14px;">
                            <span class="news-platform-tag taobao"><i class="fas fa-shopping-cart"></i> 淘宝</span>
                            <span class="news-badge-new">NEW</span>
                            <span class="news-date">2026.05.26</span>
                        </div>
                    </div>
                    <div class="news-card-body">
                        <h3 class="news-title" data-i18n="news_wuthering_title">鸣潮x雷蛇 达妮娅联动商品已上线</h3>
                        <p class="news-excerpt" data-i18n="news_wuthering_excerpt">鸣潮与雷蛇的达妮娅联名商品已在淘宝开启预售。</p>
                        <div class="news-card-footer">
                            <span class="news-category-label"><i class="fas fa-tag"></i> <span data-i18n="news_cate_shopping">ショッピング</span></span>
                            <span class="news-read-more" data-news="news_wuthering"><span data-i18n="news_readmore">続きを読む</span> <i class="fas fa-arrow-right"></i></span>
                        </div>
                    </div>
                </div>

                <!-- Article: Niko Bilibili Live Stream -->
                <div class="news-card" data-news="news_niko">"""

content = content.replace(old_cards, new_wuthering_card, 1)

# --- 2. 日语 i18n 字典：在 news_niko_title 之前插入新条目 ---
old_ja = """                news_cate_live: 'ライブ配信',
                news_niko_title: 'Niko が Bilibili で独占ライブ配信を行います','''

new_ja = """                news_cate_live: 'ライブ配信',
                news_wuthering_title: '鳴潮（Wuthering Waves）× Razer コラボ商品が発売開始',
                news_wuthering_excerpt: '鳴潮と Razer のコラボレーションによる「ダーニャ」モデル商品が、淘宝（タオバオ）にて予約販売を開始しました。中国国外への配送に対応していないため、ご興味のある方は公式サイトにて商品詳細および価格を事前にご確認ください。',
                news_niko_title: 'Niko が Bilibili で独占ライブ配信を行います','''

content = content.replace(old_ja, new_ja, 1)

# --- 3. 英语 i18n 字典：在 news_niko_title 之前插入新条目 ---
old_en = """                news_cate_live: 'Live Stream',
                news_niko_title: 'Niko to Host Exclusive Live Stream on Bilibili','''

new_en = """                news_cate_live: 'Live Stream',
                news_wuthering_title: 'Wuthering Waves × Razer Collaboration Merch Now Available',
                news_wuthering_excerpt: 'The Wuthering Waves × Razer "Denia" collaboration merchandise is now available for pre-order on Taobao. Since Taobao does not support international shipping, please visit the official website to check product details and pricing in advance.',
                news_niko_title: 'Niko to Host Exclusive Live Stream on Bilibili','''

content = content.replace(old_en, new_en, 1)

# --- 4. newsData JS 对象：在 news_niko 之前插入 news_wuthering ---
old_newsdata = """            // News modal data
            const newsData = {
                news_niko: {"""

new_newsdata = """            // News modal data
            const newsData = {
                news_wuthering: {
                    platform: 'taobao',
                    platformIcon: 'fas fa-shopping-cart',
                    platformLabel_ja: '淘宝',
                    platformLabel_en: 'Taobao',
                    date: '2026.05.26',
                    isNew: true,
                    // ★ 图片替换位置：把下面 img_src 的值换成实际新闻图片路径即可 ★
                img_src: 'https://picsum.photos/600/320?random=wuthering_razer_live',
                title_ja: '鳴潮（Wuthering Waves）× Razer コラボ商品が発売開始',
                title_en: 'Wuthering Waves × Razer Collaboration Merch Now Available',
                body_ja: `<p>『<strong>鳴潮（Wuthering Waves）</strong>』と『<strong>Razer（レーザー）</strong>』のコラボレーションによる、キャラクター「<strong>ダーニャ（Denia）</strong>」モデルの联名商品が、<strong>淘宝（タオバオ）</strong>にて予約販売を開始しました。</p>
<div class="news-highlight-box">🛍️ 販売プラットフォーム：淘宝（Taobao）<br>📦 商品：ダーニャ × Razer コラボグッズ<br>⚠️ 注意：淘宝は海外配送に対応していません</div>
<p>淘宝では国際配送に対応していない商品がほとんどのため、実際に購入を検討されている方は、まず<strong>公式サイトにて商品の詳細および価格をご確認になることをおすすめします</strong>。</p>
<p>『鳴潮』の公式サイトは以下のリンクからアクセス可能です。商品ラインナップ、価格、発送時期などの最新情報をチェックできます。</p>
<p style="margin-top:18px;"><a href="https://wutheringwaves.kurogames.com/" target="_blank" style="display:inline-flex;align-items:center;gap:8px;padding:12px 24px;background:linear-gradient(135deg,#00a1d6,#008ac7);color:#fff;text-decoration:none;border-radius:10px;font-weight:600;font-size:14px;transition:all 0.25s ease;" onmouseover="this.style.transform=\\'translateY(-2px)\\';this.style.boxShadow=\\'0 6px 20px rgba(0,161,214,0.35)\\';" onmouseout="this.style.transform=\\'\\';this.style.boxShadow=\\'none\\';"><i class="fas fa-globe"></i> 鳴潮公式サイトを見る</a></p>`,
                body_en: `<p>The collaboration merchandise featuring <strong>Denia</strong> from <strong>Wuthering Waves</strong> and <strong>Razer</strong> is now available for pre-order on <strong>Taobao</strong>.</p>
<div class="news-highlight-box">🛍️ Platform: Taobao (China only)<br>📦 Product: Denia × Razer collaboration goods<br>⚠️ Note: Taobao does not support international shipping</div>
<p>Most items on Taobao do not support international shipping. If you are considering purchasing, we strongly recommend <strong>checking the official Wuthering Waves website first for detailed product information and pricing.</strong></p>
<p>You can visit the official Wuthering Waves website via the link below to check the latest updates on product lineup, pricing, and release schedule.</p>
<p style="margin-top:18px;"><a href="https://wutheringwaves.kurogames.com/" target="_blank" style="display:inline-flex;align-items:center;gap:8px;padding:12px 24px;background:linear-gradient(135deg,#00a1d6,#008ac7);color:#fff;text-decoration:none;border-radius:10px;font-weight:600;font-size:14px;transition:all 0.25s ease;" onmouseover="this.style.transform=\\'translateY(-2px)\\';this.style.boxShadow=\\'0 6px 20px rgba(0,161,214,0.35)\\';" onmouseout="this.style.transform=\\'\\';this.style.boxShadow=\\'none\\';"><i class="fas fa-globe"></i> Visit Wuthering Waves Official Site</a></p>`
                },
                news_niko: {"""

content = content.replace(old_newsdata, new_newsdata, 1)

with open('E:/web/web.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Done! All 4 replacements completed.")
print("Image replacement positions:")
print("  1. Card HTML (line ~1345): src='https://picsum.photos/...'")
print("  2. newsData.img_src (line ~2098): img_src:'https://picsum.photos/...'")
