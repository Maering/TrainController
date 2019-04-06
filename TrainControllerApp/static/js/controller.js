function fetchAjax(url, payload)
{
    // Get CSRF Token
    var csrftok = Toolbox.getCookie('csrftoken');

    // Build headers
    var headers = new Headers();
    headers.append('X-CSRFToken', csrftok);

    // Build request body
    var data = new FormData();
    data.append("json", JSON.stringify(payload));

    // Build post params
    var init = {
        method: "POST",
        headers: headers,
        mode: 'cors',
        cache: 'default',
        body: data,
    };

    var output = "";

    // send command
    fetch(url, init)
    .then(function (response) {
        console.log(response);
        output = response;
    }).catch(function (error) {
        console.log(error);
    });

    return output;
}

function send(action, args)
{
    return fetchAjax("/controls/process", { action : action, args: args });
}

class Controller {

    constructor() {
        this.trains = [];
        this.active = false;
    }

    addTrain(id, name, lokid)
    {
        var trainID = parseInt(id);
        var trainLokID = parseInt(lokid);

        // Create new train
        var train = new Train(trainID, name, trainLokID)

        // Insert the train
        this.trains[trainID]=train;
    }

    getTrain(id)
    {
        return this.trains[parseInt(id)];
    }

    go() {
        if(send('go') == 'ok')
        {
            this.active = true; //FIXME: not securized since Intellibox could throw error
        }
        else
        {
            //TODO:
        }
    }

    stop() {
        if(send('stop') == 'ok')
        {
            this.active = false; //FIXME: not securized since Intellibox could throw error
        }
        else
        {
            //TODO:
        }
    }
}

class Train {

    constructor(id, name, lokid)
    {
        this.id = id;
        this.name = name;
        this.lokid = lokid;
        this.speed = 0;
        this.forward = true;
        this.lights = false;
        this.f1 = false;
        this.f2 = false;
        this.f3 = false;
        this.f4 = false;

        this.register();
    }

    register() {
        var result = send('register', { what: 'train', name: this.name, address: this.lokid });
        if(result == 'ok')
        {
            //TODO: //FIXME: not securized since Intellibox could throw error
        }
        else
        {
            console.log("[register]:"+result);
            //TODO:
        }
    }

    accelerate() {
        var result = send('train', { action:'accelerate', lokid: this.lokid });
        if(result == 'ok')
        {
            //TODO: //FIXME: not securized since Intellibox could throw error
        }
        else
        {
            console.log("[accelerate]:"+result);
            //TODO:
        }
    }
    decelerate() {
        if(send('train', { action:'decelerate', lokid: this.lokid }) == 'ok')
        {
            //TODO: //FIXME: not securized since Intellibox could throw error
        }
        else
        {
            //TODO:
        }
    }
    reverse() {
        if(send('train', { action:'reverse', lokid: this.lokid }) == 'ok')
        {
            //TODO: //FIXME: not securized since Intellibox could throw error
        }
        else
        {
            //TODO:
        }
    }
    toggleLights() {
        if(send('train', { action:'togglelights', lokid: this.lokid }) == 'ok')
        {
            //TODO: //FIXME: not securized since Intellibox could throw error
        }
        else
        {
            //TODO:
        }
    }
    toggleF1() {
        if(send('train', { action:'togglef1', lokid: this.lokid }) == 'ok')
        {
            //TODO: //FIXME: not securized since Intellibox could throw error
        }
        else
        {
            //TODO:
        }
    }
    toggleF2() {
        if(send('train', { action:'togglef2', lokid: this.lokid }) == 'ok')
        {
            //TODO: //FIXME: not securized since Intellibox could throw error
        }
        else
        {
            //TODO:
        }
    }
    toggleF3() {
        if(send('train', { action:'togglef3', lokid: this.lokid }) == 'ok')
        {
            //TODO: //FIXME: not securized since Intellibox could throw error
        }
        else
        {
            //TODO:
        }
    }
    toggleF4() {
        if(send('train', { action:'togglef4', lokid: this.lokid }) == 'ok')
        {
            //TODO: //FIXME: not securized since Intellibox could throw error
        }
        else
        {
            //TODO:
        }
    }
    toString() {
        var data = [];
        data.push(
            "[",
            this.id,
            "]: name: ",
            this.name,
            ", lokid: ",
            this.lokid
        );
        return data.join("");
    }
}