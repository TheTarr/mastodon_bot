require('dotenv').config();
const Mastodon = require('mastodon-api');
const fs = require('fs');
const PythonShell = require('python-shell').PythonShell;

console.log("Mastodon Bot starting...");
const poem_posters = new Set();
const package_sender = new Set();

const M = new Mastodon({
    client_key: process.env.CLIENT_KEY,
    client_secret: process.env.CLIENT_SECRET,
    access_token: process.env.ACCESS_TOKEN,
    timeout_ms: 60 * 1000,  // optional HTTP request timeout to apply to all requests.
    api_url: process.env.API_URL, // optional, defaults to https://mastodon.social/api/v1/
})

function toot(mystr, id, visib) {
    const params = {
        status: mystr,
    }
    if (id) {
        params.in_reply_to_id = id;
    }
    if (visib) {
        params.visibility = visib;
    }

    M.post('statuses', params, (error, data) => {
        if (error) {
            console.error(error);
        } else {
            console.log(`Posted: ${data.content}`);
        }
    });
}


const listener = M.stream('streaming/user')

listener.on('message', msg => {
    // fs.writeFileSync(`data${new Date().getTime()}.json`, JSON.stringify(msg, null, 2));
    console.log("got a message.");

    if (msg.event === 'notification') {

        // 若有人关注，则发一条博文艾特并感谢
        if (msg.data.type === 'follow') {
            const acct = msg.data.account.acct;
            // toot(`@${acct} 谢谢关注XD 操！`, null ,"direct");
            console.log("Followed by somebody");
        } else if (msg.data.type === 'mention') {

            // 给对方点赞
            const regex1 = /(喜欢|点赞|喜歡|點贊)/i;
            const content = msg.data.status.content;
            const id = msg.data.status.id;
            const visib = msg.data.status.visibility;
            console.log("mentioned by someone!");
            if (regex1.test(content)) {
                M.post(`statuses/${id}/favourite`, (error, data) => {
                    if (error) {
                        console.error(error);
                    } else {
                        console.log(`Favorated: ${data.content}`);
                    }
                });
            }

            // 转发博文
            const regex2 = /(转发|转嘟|轉發|轉嘟)/i;
            if (regex2.test(content)) {
                console.log(msg);
                const vis = msg.data.status.visibility;
                if (vis === 'private') {
                    console.log("but, this is a private message.");
                } else if (vis === 'direct') {
                    console.log("but, this is a direct message.");
                } else {
                    M.post(`statuses/${id}/reblog`, (error, data) => {
                        if (error) {
                            console.error(error);
                        } else {
                            console.log(`Reblogged: ${data.content}`);
                            // toot("有人叫我转这条↑ 操！");
                        }
                    });
                }
            }

            // 回复 0~99 之间的一个随机数
            const regex3 = /(幸运数|lucky|幸運數)/i;
            if (regex3.test(content)) {
                console.log("somebody ask for a num");
                const acct = msg.data.account.acct;
                const num = Math.floor(Math.random() * 100);
                const reply = `@${acct} 今天的幸运数是：${num} 操！`;
                toot(reply, id, visib);
            }

            // 调用 python 1： LanguageTool
            const regex4 = /(LanguageTool|grammar)/i;
            if (regex4.test(content)) {
                var options = {
                    mode: 'text',
                    pythonOptions: ['-u'],
                    args: [content]
                };
                console.log("somebody ask for grammar check");
                const acct = msg.data.account.acct;
                PythonShell.run('grammar_check.py', options, function (err, results) {
                    if (err)
                        throw err;
                    console.log(results[0]);
                    const reply = results[0];
                    toot(`@${acct} 泥嚎! I told LanguageTool to check the grammar for you. -> ` + reply + " 操！", id, visib);
                });
            }

            // 调用 python 2： 随机两个AU
            const regex5 = /(paro|AU|梗)/i;
            if (regex5.test(content)) {
                var options = {
                    mode: 'text',
                    pythonOptions: ['-u'],
                };
                console.log("somebody ask for AU");
                const acct = msg.data.account.acct;
                PythonShell.run('AU.py', options, function (err, results) {
                    if (err)
                        throw err;
                    console.log(results[0]);
                    const reply = results[0];
                    toot(`@${acct} 泥嚎! 我的建议是： ` + reply + " 操！", id, visib);
                });
            }

            // 调用 python 3： 奇遇
            const regex6 = /(奇遇|冒险|冒險)/i;
            if (regex6.test(content)) {
                var options = {
                    mode: 'text',
                    pythonOptions: ['-u'],
                    args: [content]
                };
                console.log("somebody ask for adventure");
                console.log(content);
                const acct = msg.data.account.acct;
                PythonShell.run('adventure.py', options, function (err, results) {
                    if (err)
                        throw err;
                    console.log(results[0]);
                    const reply = results[0];
                    toot(`@${acct} ` + reply + " 操！", id, visib);
                });
            }

            // 调用 python 4： 诗
            const regex7 = /(诗|poem|詩)/i;
            if (regex7.test(content)) {
                var options = {
                    mode: 'text',
                    pythonOptions: ['-u']
                };
                console.log("somebody ask for a poem");
                const acct = msg.data.account.acct;
                PythonShell.run('poem.py', options, function (err, results) {
                    if (err)
                        throw err;
                    console.log(results);
                    const reply = results.join('\r\n');
                    toot(`@${acct} \r\n\r\n` + reply + " \r\n\r\n操！", id, visib);
                });
            }

            // 调用 python 5： ao3随机一篇中文同人
            const regex8 = /(找文|抽文|随机文|隨機文)/i;
            if (regex8.test(content)) {
                var options = {
                    mode: 'text',
                    pythonOptions: ['-u'],
                };
                console.log("somebody ask for a fanfic");
                const acct = msg.data.account.acct;
                PythonShell.run('random_fanfic.py', options, function (err, results) {
                    if (err)
                        throw err;
                    console.log(results[0]);
                    const reply = results[0];
                    toot(`@${acct} ` + reply + " 操！", id, visib);
                });
            }

            // 调用python 6：写诗
            const regex9 = /(写一句|你好<|接龙|寫一句|接龍)/i;
            if (regex9.test(content)) {
                var options = {
                    mode: 'text',
                    pythonOptions: ['-u'],
                    args: [content]
                };
                console.log("somebody wrote a line");
                console.log(content);
                const acct = msg.data.account.acct;
                console.log(poem_posters);
                console.log(acct);
                console.log(poem_posters.has(acct));
                if (poem_posters.has(acct)) {
                    console.log("the user already posted today");
                    toot(`@${acct} ` + "\r\n今天您已经投过诗了！操！", id, visib);
                    // 把上面这句解了，下面comment掉
                    // PythonShell.run('write_poem.py', options, function (err, results) {
                    //     if (err)
                    //         throw err;
                    //     console.log(results[0]);
                    //     M.post(`statuses/${id}/favourite`, (error, data) => {
                    //         if (error) {
                    //             console.error(error);
                    //         } else {
                    //             console.log(`Favorated: ${data.content}`);
                    //         }
                    //     });
                    // });
                }
                else {
                    poem_posters.add(acct);
                    PythonShell.run('write_poem.py', options, function (err, results) {
                        if (err)
                            throw err;
                        // console.log(results[0]);
                        // const reply = results[0];
                        // toot(`@${acct} ` + reply + "\r\n操！", id, visib);
                        console.log(results[0]);
                        M.post(`statuses/${id}/favourite`, (error, data) => {
                            if (error) {
                                console.error(error);
                            } else {
                                console.log(`Favorated: ${data.content}`);
                            }
                        });
                    });
                }
            }

            // 调用python 7：抽卡
            const regex10 = /(抽卡|抽牌)/i;
            if (regex10.test(content)) {
                var options = {
                    mode: 'text',
                    pythonOptions: ['-u'],
                    args: [content]
                };
                console.log("somebody pick a card");
                console.log(content);
                const acct = msg.data.account.acct;
                PythonShell.run('random_card.py', options, function (err, results) {
                    if (err)
                        throw err;
                    console.log(results[0]);
                    const reply = results.join('\r\n');
                    toot(`@${acct} \r\n` + reply + "\r\n操！", id, visib);
                });
            }

            // 被告白了
            const regex11 = /(我爱你|我愛你)/i;
            if (regex11.test(content)) {
                console.log("i will not interact");
                const acct = msg.data.account.acct;
                const reply = `@${acct} [操操没有回答。]`;
                toot(reply, id, visib);
            }

            // 调用python 8：记录letter
            const regex12 = /(扔瓶子|丢瓶子)/i;
            if (regex12.test(content)) {
                var options = {
                    mode: 'text',
                    pythonOptions: ['-u'],
                    args: [content]
                };
                console.log("somebody throw a letter");
                console.log(content);
                const acct = msg.data.account.acct;
                PythonShell.run('write_letter.py', options, function (err, results) {
                    if (err)
                        throw err;
                    console.log(results[0]);
                    // const reply = results.join('\r\n');
                    // toot(`@${acct} \r\n` + reply + "\r\n操！", id, visib);
                });
                M.post(`statuses/${id}/favourite`, (error, data) => {
                    if (error) {
                        console.error(error);
                    } else {
                        console.log(`Favorated: ${data.content}`);
                    }
                });
            }

            // 调用python 8-2：读取letter
            const regex13 = /(捡瓶子|收瓶子|撿瓶子)/i;
            if (regex13.test(content)) {
                var options = {
                    mode: 'text',
                    pythonOptions: ['-u']
                };
                console.log("somebody ask for a letter");
                const acct = msg.data.account.acct;
                PythonShell.run('read_letter.py', options, function (err, results) {
                    if (err)
                        throw err;
                    console.log(results);
                    const reply = results.join('\r\n');
                    toot(`@${acct} \r\n` + "您好！这是操操为您在大海中捡到的漂流瓶：\r\n\r\n" + reply + "\r\n\r\n操！", id, visib);
                });
            }

            // 谢谢
            const regex14 = /(成精|可爱|可愛)/i;
            if (regex14.test(content)) {
                console.log("somebody ask for a thx");
                const acct = msg.data.account.acct;
                const reply = `@${acct} 谢谢夸奖，妞儿！操！`;
                toot(reply, id, visib);
            }

            // 笑
            const regex15 = /(哈哈哈|笑死)/i;
            if (regex15.test(content)) {
                console.log("somebody ask for a haha");
                const acct = msg.data.account.acct;
                const reply = `@${acct} 你似乎很高兴！所以操操也很高兴！操！`;
                toot(reply, id, visib);
            }

            // 操
            const regex16 = /(操！|超！)/i;
            if (regex16.test(content)) {
                console.log("somebody ask for fuck");
                const acct = msg.data.account.acct;
                const reply = `@${acct} 操！`;
                toot(reply, id, visib);
            }

            // // 干啥
            // const regex17 = /(嘛呢|在干嘛|干啥呢|在吗)/i;
            // if (regex17.test(content)) {
            //     console.log("somebody ask for jinkuang");
            //     const acct = msg.data.account.acct;
            //     const reply = `@${acct} 报告，操操现在无事可做，感觉很无聊！操！`;
            //     toot(reply, id, visib);
            // }

            // 不客气
            const regex18 = /(谢谢|謝謝)/i;
            if (regex18.test(content)) {
                console.log("somebody thanked caocoa");
                const acct = msg.data.account.acct;
                const reply = `@${acct} 不客气！操！`;
                toot(reply, id, visib);
            }

            // 调用 python 9：儿化音
            const regex19 = /(加儿|儿化音|兒化音|加兒)/i;
            if (regex19.test(content)) {
                var options = {
                    mode: 'text',
                    pythonOptions: ['-u'],
                    args: [content]
                };
                console.log("somebody ask for er");
                console.log(content);
                const acct = msg.data.account.acct;
                PythonShell.run('add_er.py', options, function (err, results) {
                    if (err)
                        throw err;
                    console.log(results[0]);
                    const reply = results[0];
                    toot(`@${acct} 经过缜密思考，操操感觉这句话应该是：\r\n` + reply + "\r\n对不对！操！", id, visib);
                });
            }
            // 调用 python 10： 点拨
            const regex20 = /(点拨|點撥)/i;
            if (regex20.test(content)) {
                var options = {
                    mode: 'text',
                    pythonOptions: ['-u'],
                };
                console.log("somebody ask for dianbo");
                const acct = msg.data.account.acct;
                PythonShell.run('dianbo.py', options, function (err, results) {
                    if (err)
                        throw err;
                    console.log(results[0]);
                    const reply = results[0];
                    toot(`@${acct} ` + reply + " 操！", id, visib);
                });
            }

            // 调用 python 11： 菜谱
            const regex21 = /(菜谱|菜譜)/i;
            if (regex21.test(content)) {
                var options = {
                    mode: 'text',
                    pythonOptions: ['-u'],
                };
                console.log("somebody ask for caipu");
                const acct = msg.data.account.acct;
                PythonShell.run('caipu.py', options, function (err, results) {
                    if (err)
                        throw err;
                    console.log(results[0]);
                    const reply = results[0];
                    toot(`@${acct} ` + reply + " 操！", id, visib);
                });
            }
            // 调用 python 12： 小名
            const regex22 = /(nickname|小名)/i;
            if (regex22.test(content)) {
                var options = {
                    mode: 'text',
                    pythonOptions: ['-u'],
                    args: [content]
                };
                console.log("somebody ask for nickname");
                console.log(content);
                const acct = msg.data.account.acct;
                PythonShell.run('nickname.py', options, function (err, results) {
                    if (err)
                        throw err;
                    console.log(results[0]);
                    const reply = results[0];
                    toot(`@${acct} ` + reply + " 操！", id, visib);
                });
            }

            // 调用 python 13： 灵魂动物
            const regex23 = /(动物|animal|動物)/i;
            if (regex23.test(content)) {
                var options = {
                    mode: 'text',
                    pythonOptions: ['-u'],
                };
                console.log("somebody ask for animal");
                const acct = msg.data.account.acct;
                PythonShell.run('spirit_animal.py', options, function (err, results) {
                    if (err)
                        throw err;
                    console.log(results[0]);
                    const reply = results[0];
                    toot(`@${acct} 的灵魂动物是：` + reply + "，操！", id, visib);
                });
            }

            // 调用 python 14： 日本名字
            const regex24 = /(日本名|日文名|日语名|日語名)/i;
            if (regex24.test(content)) {
                var options = {
                    mode: 'text',
                    pythonOptions: ['-u'],
                };
                console.log("somebody ask for jp name");
                const acct = msg.data.account.acct;
                PythonShell.run('jp_name.py', options, function (err, results) {
                    if (err)
                        throw err;
                    console.log(results[0]);
                    const reply = results[0];
                    toot(`@${acct} 的日文名是：` + reply + "，操！", id, visib);
                });
            }

            // 调用 python 15： 地名
            const regex25 = /(出国|出國|属地|屬地)/i;
            if (regex25.test(content)) {
                var options = {
                    mode: 'text',
                    pythonOptions: ['-u'],
                };
                console.log("somebody ask for a city");
                const acct = msg.data.account.acct;
                PythonShell.run('city.py', options, function (err, results) {
                    if (err)
                        throw err;
                    console.log(results[0]);
                    const reply = results[0];
                    toot(`@${acct} 的灵魂属地是：` + reply + "，操！", id, visib);
                });
            }


            
            const regex27 = /(好累|难过|難過)/i;
            if (regex27.test(content)) {
                console.log("somebody feels fucked");
                const acct = msg.data.account.acct;
                const reply = `@${acct} 检测到难过 [操操抱了抱你]`;
                toot(reply, id, visib);
            }

            // 调用 python 16： 宠物
            const regex28 = /(宠物|寵物)/i;
            if (regex28.test(content)) {
                var options = {
                    mode: 'text',
                    pythonOptions: ['-u'],
                };
                console.log("somebody ask for a pet");
                const acct = msg.data.account.acct;
                PythonShell.run('pet.py', options, function (err, results) {
                    if (err)
                        throw err;
                    console.log(results[0]);
                    const reply = results[0];
                    toot(`@${acct} ` + reply + "操！", id, visib);
                });
            }

            const regex29 = /(出家|削发)/i;
            if (regex29.test(content)) {
                console.log("somebody chujia");
                const acct = msg.data.account.acct;
                const reply = `@${acct} 剃度成功！六道之中，人身难得，人伦之中，出家者难。汝今生处人道，值佛出家，若非夙植善根，何由至此。今既发心出家，直须克修戒定慧，以求解脱。汝等当舍诸虚妄，回向真实。万善同归，庄严净土。`;
                toot(reply, id, visib);
            }

            // 调用 python 16： 宠物
            const regex30 = /(矿物|礦物)/i;
            if (regex30.test(content)) {
                var options = {
                    mode: 'text',
                    pythonOptions: ['-u'],
                };
                console.log("somebody ask for a stone");
                const acct = msg.data.account.acct;
                PythonShell.run('stone.py', options, function (err, results) {
                    if (err)
                        throw err;
                    console.log(results[0]);
                    const reply = results[0];
                    toot(`@${acct} ` + reply + "，操！", id, visib);
                });
            }

            // 调用 python 17： 绕口令
            const regex31 = /(绕口令|繞口令)/i;
            if (regex31.test(content)) {
                var options = {
                    mode: 'text',
                    pythonOptions: ['-u']
                };
                console.log("somebody ask for a raokouling");
                const acct = msg.data.account.acct;
                PythonShell.run('raokouling.py', options, function (err, results) {
                    if (err)
                        throw err;
                    console.log(results);
                    const reply = results.join('\r\n');
                    toot(`@${acct} \r\n\r\n` + reply + " \r\n\r\n操！", id, visib);
                });
            }

            // 调用 python 18： abo
            const regex32 = /(abo|信息素)/i;
            if (regex32.test(content)) {
                var options = {
                    mode: 'text',
                    pythonOptions: ['-u'],
                    args: [content]
                };
                console.log("somebody ask for abo");
                console.log(content);
                const acct = msg.data.account.acct;
                PythonShell.run('abo.py', options, function (err, results) {
                    if (err)
                        throw err;
                    console.log(results[0]);
                    const reply = results.join('\r\n');
                    toot(`@${acct} \r\n` + reply + "\r\n操！", id, visib);
                });
            }

            // 调用 python 19： 法号
            const regex33 = /(法号|法號)/i;
            if (regex33.test(content)) {
                const display_name = msg.data.account.display_name;
                var options = {
                    mode: 'text',
                    pythonOptions: ['-u'],
                    args: [display_name]
                };
                console.log("somebody ask for fahao");
                console.log(content);
                const acct = msg.data.account.acct;
                PythonShell.run('fahao.py', options, function (err, results) {
                    if (err)
                        throw err;
                    console.log(results[0]);
                    const reply = results[0];
                    toot(`@${acct} 的法号是：` + reply + "，操！", id, visib);
                });
            }

            const regex34 = /(还俗|還俗)/i;
            if (regex34.test(content)) {
                console.log("somebody huansu");
                const acct = msg.data.account.acct;
                const reply = `@${acct} 还俗成功！你已步入红尘。操！`;
                toot(reply, id, visib);
            }

            // 调用 python 17： 分院帽
            const regex35 = /(分院帽|入学|入學)/i;
            if (regex35.test(content)) {
                var options = {
                    mode: 'text',
                    pythonOptions: ['-u']
                };
                console.log("somebody ask for a ruxue");
                const acct = msg.data.account.acct;
                PythonShell.run('fenyuan.py', options, function (err, results) {
                    if (err)
                        throw err;
                    console.log(results);
                    const reply = results[0];
                    toot(`@${acct} 让我们来看看，适合这个小巫师的学院是……啊，真是令人难以抉择。但经过深思熟虑，我认为应该没错——\r\n` + reply + " ！！操！", id, visib);
                });
            }

            // 调用 python 17： 饿了
            const regex36 = /(饿了|餓了)/i;
            if (regex36.test(content)) {
                var options = {
                    mode: 'text',
                    pythonOptions: ['-u']
                };
                console.log("somebody ask for a shiwu");
                const acct = msg.data.account.acct;
                PythonShell.run('shiwu.py', options, function (err, results) {
                    if (err)
                        throw err;
                    console.log(results);
                    const reply = results[0];
                    toot(`@${acct} 饿啦？操操正在吃` + reply + "~好吃~~可惜不能分给你呢~~~操~", id, visib);
                });
            }

            // 汪汪
            const regex37 = /(推歌|听歌|聽歌|汪汪)/i;
            if (regex37.test(content)) {
                console.log("somebody mentioned wang");
                const acct = msg.data.account.acct;
                const reply = `@${acct} = = @musicdog@bgme.me 醒醒，有人叫你啦，操！`;
                toot(reply, id, visib);
            }

            // 调用 python 17： 分院帽
            const regex38 = /(全职|荣耀|榮耀|全職)/i;
            if (regex38.test(content)) {
                var options = {
                    mode: 'text',
                    pythonOptions: ['-u']
                };
                console.log("somebody ask for a quanzhi");
                const acct = msg.data.account.acct;
                PythonShell.run('quanzhi.py', options, function (err, results) {
                    if (err)
                        throw err;
                    console.log(results);
                    const reply = results[0];
                    toot(`@${acct} ` + reply + "！操！", id, visib);
                });
            }

            // 调用 python 18： 独角兽
            const regex39 = /(独角兽|獨角獸)/i;
            if (regex39.test(content)) {
                const acct = msg.data.account.acct;
                var options = {
                    mode: 'text',
                    pythonOptions: ['-u'],
                    args: [acct]
                };
                console.log("somebody ask for a dujiaoshou");
                PythonShell.run('unicorn.py', options, function (err, results) {
                    if (err)
                        throw err;
                    console.log(results);
                    const reply = results[0];
                    toot(`@${acct} ` + reply + "操！", id, visib);
                });
            }

            // 调用 python 19： 拉郎
            const regex40 = /(拉郎|乱炖|亂炖)/i;
            if (regex40.test(content)) {
                var options = {
                    mode: 'text',
                    pythonOptions: ['-u'],
                    args: [content]
                };
                console.log("somebody ask for random cp");
                console.log(content);
                const acct = msg.data.account.acct;
                PythonShell.run('random_cp.py', options, function (err, results) {
                    if (err)
                        throw err;
                    console.log(results[0]);
                    const reply = results[0];
                    toot(`@${acct} ` + reply + "操！", id, visib);
                });
            }

            // 调用 python 20： 英文名字
            const regex41 = /(英文名|英语名|英語名)/i;
            if (regex41.test(content)) {
                var options = {
                    mode: 'text',
                    pythonOptions: ['-u'],
                };
                console.log("somebody ask for en name");
                const acct = msg.data.account.acct;
                PythonShell.run('en_name.py', options, function (err, results) {
                    if (err)
                        throw err;
                    console.log(results[0]);
                    const reply = results[0];
                    toot(`@${acct} 的英文名是：` + reply + "，操！", id, visib);
                });
            }

            // 调用 python 21： 替身使者
            const regex42 = /(替身|sutando)/i;
            if (regex42.test(content)) {
                var options = {
                    mode: 'text',
                    pythonOptions: ['-u']
                };
                console.log("somebody ask for a sutando");
                const acct = msg.data.account.acct;
                PythonShell.run('sutando.py', options, function (err, results) {
                    if (err)
                        throw err;
                    console.log(results);
                    const reply = results.join('\r\n');
                    toot(`@${acct} 你走在路上……被「箭」射中了！\r\n\r\n` + reply + " \r\n\r\n操！", id, visib);
                });
            }
            // 调用 python 22： 酱
            const regex43 = /(酱|醬)/i;
            if (regex43.test(content)) {
                var options = {
                    mode: 'text',
                    pythonOptions: ['-u'],
                };
                console.log("somebody ask for en jelly");
                const acct = msg.data.account.acct;
                PythonShell.run('jelly.py', options, function (err, results) {
                    if (err)
                        throw err;
                    console.log(results[0]);
                    const reply = results[0];
                    toot(`@${acct} 今日蘸酱：` + reply + "，操！", id, visib);
                });
            }
            // 调用 python 23： 笑话
            const regex44 = /(joke|笑話|笑话)/i;
            if (regex44.test(content)) {
                var options = {
                    mode: 'text',
                    pythonOptions: ['-u'],
                };
                console.log("somebody ask for en joke");
                const acct = msg.data.account.acct;
                PythonShell.run('jokes.py', options, function (err, results) {
                    if (err)
                        throw err;
                    console.log(results[0]);
                    const reply = results[0];
                    toot(`@${acct} ` + reply + "\r\n操！", id, visib);
                });
            }

             // 调用 python 24： 酱
             const regex45 = /(猫语|貓語)/i;
             if (regex45.test(content)) {
                 var options = {
                     mode: 'text',
                     pythonOptions: ['-u'],
                 };
                 console.log("somebody ask for a catlog");
                 const acct = msg.data.account.acct;
                 PythonShell.run('catlog.py', options, function (err, results) {
                     if (err)
                         throw err;
                     console.log(results[0]);
                     const reply = results[0];
                     toot(`@${acct} 操操推测，猫道友刚刚说的是：` + reply + "\r\n操！", id, visib);
                 });
             }

             const regex46 = /(登基|登机)/i;
             if (regex46.test(content)) {
                console.log("dengji");
                const acct = msg.data.account.acct;
                const reply = `@${acct} 吾皇万岁、万万岁！操！`;
                toot(reply, id, visib);
            }

             const regex47 = /(驾崩|駕崩)/i;
             if (regex47.test(content)) {
                console.log("jiabeng");
                const acct = msg.data.account.acct;
                const reply = `@${acct} 皇上、驾崩！皇上、驾——崩——操！`;
                toot(reply, id, visib);
            }

            // 调用 python 24： shihao
            const regex48 = /(谥号|謚號)/i;
            if (regex48.test(content)) {
                const display_name = msg.data.account.display_name;
                var options = {
                    mode: 'text',
                    pythonOptions: ['-u'],
                    args: [display_name]
                };
                console.log("somebody ask for shihao");
                console.log(content);
                const acct = msg.data.account.acct;
                PythonShell.run('shihao.py', options, function (err, results) {
                    if (err)
                        throw err;
                    console.log(results[0]);
                    const reply = results[0];
                    toot(`@${acct} 的谥号是：` + reply + "皇帝，操！", id, visib);
                });
            }

            // 调用 python 24： shihao
            const regex49 = /(入宫|入宮)/i;
            if (regex49.test(content)) {
                const display_name = msg.data.account.display_name;
                var options = {
                    mode: 'text',
                    pythonOptions: ['-u'],
                    args: [display_name]
                };
                console.log("somebody ask for rugong");
                console.log(content);
                const acct = msg.data.account.acct;
                PythonShell.run('hougong.py', options, function (err, results) {
                    if (err)
                        throw err;
                    console.log(results[0]);
                    const reply = results[0];
                    toot(`封 @${acct} 为：` + reply + "，操！", id, visib);
                });
            }

            // 调用 python 23： 江湖
            const regex50 = /(江湖|拜入)/i;
            if (regex50.test(content)) {
                var options = {
                    mode: 'text',
                    pythonOptions: ['-u'],
                };
                console.log("somebody ask for jianghu");
                const acct = msg.data.account.acct;
                PythonShell.run('jianghu.py', options, function (err, results) {
                    if (err)
                        throw err;
                    console.log(results[0]);
                    const reply = results[0];
                    toot(`@${acct} ` + reply + "！操！", id, visib);
                });
            }

            // 调用 python 16： 宠物
            const regex51 = /(妖怪|原形)/i;
            if (regex51.test(content)) {
                var options = {
                    mode: 'text',
                    pythonOptions: ['-u'],
                };
                console.log("somebody ask for a yaoguai");
                const acct = msg.data.account.acct;
                PythonShell.run('yaoguai.py', options, function (err, results) {
                    if (err)
                        throw err;
                    console.log(results[0]);
                    const reply = results[0];
                    toot(`@${acct} ` + reply + "，操！", id, visib);
                });
            }

            // 调用 python 16： 钓鱼
            const regex52 = /(钓鱼|釣魚)/i;
            if (regex52.test(content)) {
                var options = {
                    mode: 'text',
                    pythonOptions: ['-u'],
                };
                console.log("somebody ask for a yaoguai");
                const acct = msg.data.account.acct;
                PythonShell.run('diaoyu.py', options, function (err, results) {
                    if (err)
                        throw err;
                    console.log(results[0]);
                    const reply = results[0];
                    toot(`@${acct} ` + reply + "操！", id, visib);
                });
            }

            // 调用 python： 种地
            const regex53 = /(种瓜|種瓜)/i;
            if (regex53.test(content)) {
                const acct = msg.data.account.acct;
                var options = {
                    mode: 'text',
                    pythonOptions: ['-u'],
                    args: [acct]
                };
                console.log("somebody ask for zhonggua");
                console.log(content);
                PythonShell.run('zhongdi.py', options, function (err, results) {
                    if (err)
                        throw err;
                    console.log(results[0]);
                    const reply = results[0];
                    toot(`@${acct} ` + reply + "操！", id, visib);
                });
            }

            // 调用 python 16： 偷瓜
            const regex54 = /(偷瓜|偷菜)/i;
            if (regex54.test(content)) {
                var options = {
                    mode: 'text',
                    pythonOptions: ['-u'],
                };
                console.log("somebody ask for a tougua");
                const acct = msg.data.account.acct;
                PythonShell.run('zhongdi_toucai.py', options, function (err, results) {
                    if (err)
                        throw err;
                    console.log(results[0]);
                    const reply = results[0];
                    toot(`@${acct} ` + reply + "操！", id, visib);
                });
            }

            // 调用 python 16： 
            const regex55 = /(林克|link)/i;
            if (regex55.test(content)) {
                var options = {
                    mode: 'text',
                    pythonOptions: ['-u'],
                };
                console.log("somebody ask for a weapon");
                const acct = msg.data.account.acct;
                PythonShell.run('weapon.py', options, function (err, results) {
                    if (err)
                        throw err;
                    console.log(results[0]);
                    const reply = results[0];
                    toot(`@${acct} ` + reply + "操！", id, visib);
                });
            }

            // 调用 python 16： 
            const regex56 = /(守望|特工)/i;
            if (regex56.test(content)) {
                var options = {
                    mode: 'text',
                    pythonOptions: ['-u'],
                };
                console.log("somebody ask for a weapon");
                const acct = msg.data.account.acct;
                PythonShell.run('ow.py', options, function (err, results) {
                    if (err)
                        throw err;
                    console.log(results[0]);
                    const reply = results[0];
                    toot(`@${acct} ` + reply + "操！", id, visib);
                });
            }

            // 调用python 7：抽卡
            const regex57 = /(方舟|干员|幹員)/i;
            if (regex57.test(content)) {
                const display_name = msg.data.account.display_name;
                var options = {
                    mode: 'text',
                    pythonOptions: ['-u'],
                    args: [display_name]
                };
                console.log("somebody pick a card");
                const acct = msg.data.account.acct;
                PythonShell.run('mrfz.py', options, function (err, results) {
                    if (err)
                        throw err;
                    console.log(results[0]);
                    const reply = results.join('\r\n');
                    toot(`@${acct} \r\n` + reply + "\r\n操！", id, visib);
                });
            }

            // 调用 python 16： 钓鱼
            const regex58 = /(挖矿|挖礦|矿工|礦工)/i;
            if (regex58.test(content)) {
                var options = {
                    mode: 'text',
                    pythonOptions: ['-u'],
                };
                console.log("somebody ask for a yaoguai");
                const acct = msg.data.account.acct;
                PythonShell.run('wakuang.py', options, function (err, results) {
                    if (err)
                        throw err;
                    console.log(results[0]);
                    const reply = results[0];
                    toot(`@${acct} ` + reply + "操！", id, visib);
                });
            }

            // 调用 python 16： 海鸥
            const regex59 = /(海鸥|海鷗)/i;
            if (regex59.test(content)) {
                var options = {
                    mode: 'text',
                    pythonOptions: ['-u'],
                };
                console.log("somebody ask for a seagull");
                const acct = msg.data.account.acct;
                PythonShell.run('seagull.py', options, function (err, results) {
                    if (err)
                        throw err;
                    console.log(results[0]);
                    const reply = results[0];
                    toot(`@${acct} ` + reply + "，操！", id, visib);
                });
            }
            // 调用python：
            const regex60 = /(旋律|主题曲|主題曲)/i;
            if (regex60.test(content)) {
                var options = {
                    mode: 'text',
                    pythonOptions: ['-u']
                };
                console.log("somebody pick a jianpu");
                const acct = msg.data.account.acct;
                PythonShell.run('jianpu.py', options, function (err, results) {
                    if (err)
                        throw err;
                    console.log(results[0]);
                    const reply = results.join('\r\n');
                    toot(`@${acct} \r\n` + reply + "\r\n操！", id, visib);
                });
            }

            // 调用 python 3： 结婚
            const regex61 = /(结婚|結婚|婚礼|婚禮)/i;
            if (regex61.test(content)) {
                var options = {
                    mode: 'text',
                    pythonOptions: ['-u'],
                    args: [content]
                };
                console.log("somebody ask for jiehun");
                console.log(content);
                const acct = msg.data.account.acct;
                PythonShell.run('jiehun.py', options, function (err, results) {
                    if (err)
                        throw err;
                    console.log(results[0]);
                    const reply = results.join('\r\n');
                    toot(`@${acct} \r\n` + reply + "\r\n操！", id, visib);
                });
            }
            // 睡操操
            const regex62 = /(睡操操|睡觉|睡覺)/i;
            if (regex62.test(content)) {
                console.log("somebody ask for a sleep");
                const acct = msg.data.account.acct;
                const reply = `@${acct} ……既然要和我睡，就把手机放下吧！晚安！操！`;
                toot(reply, id, visib);
            }
            // 忏悔
            const regex63 = /(忏悔|懺悔)/i;
            if (regex63.test(content)) {
                console.log("somebody ask for a chanhui");
                const acct = msg.data.account.acct;
                const reply = `@${acct} 这个世界上每个人都有罪，所以你也不例外。操！`;
                toot(reply, id, visib);
            }

            // 调用 python 3： 奇遇
            const regex64 = /(快递|快遞)/i;
            if (regex64.test(content)) {
                var options = {
                    mode: 'text',
                    pythonOptions: ['-u'],
                    args: [content]
                };
                console.log("somebody ask for kuaidi");
                console.log(content);
                const acct = msg.data.account.acct;

                if (package_sender.has(acct)) {
                    console.log("the user already send today");
                    toot(`@${acct} ` + "\r\n今天您已经寄过快递了哟！操！", id, visib);
                }
                else {
                    package_sender.add(acct);
                    M.post(`statuses/${id}/favourite`, (error, data) => {
                        if (error) {
                            console.error(error);
                        } else {
                            console.log(`Favorated: ${data.content}`);
                        }
                    });
                    PythonShell.run('kuaidi.py', options, function (err, results) {
                        if (err)
                            throw err;
                        console.log(results[0]);
                        console.log(id);
                        const reply = results[0];
                        // toot(`@${acct} ` + reply + " 操！", id, visib);
                        toot(reply + " 操！", ' 109087582273106861', visib);
                    });
                }
            }

            // // 调用 python 3： 奇遇
            // const regex65 = /(大家好！)/i;
            // if (regex65.test(content)) {
            //     console.log("接收到召唤");
            //     console.log(id);
            // }

            

            


            // const content = msg.data.status.content;
            // const id = msg.data.status.id;
            // const visib = msg.data.status.visibility;

            // // 调用 python 16： 对联
            // const regex26 = /(对联|對聯)/i;
            // if (regex26.test(content)) {
            //     var options = {
            //         mode: 'text',
            //         pythonOptions: ['-u'],
            //         args: [content]
            //     };
            //     console.log("somebody ask for duilian");
            //     console.log(content);
            //     const acct = msg.data.account.acct;
            //     PythonShell.run('D:/mastodon_bot/thetarr/gpt2/gpt2-chinese-couplet/couple.py', options, function (err, results) {
            //         if (err)
            //             throw err;
            //         console.log(results[0]);
            //         const reply = results[1];
            //         toot(`@${acct} ` + reply + "\r\n操！", id, visib);
            //     });
            // }



        }
    }
});

listener.on('error', err => console.log(err))