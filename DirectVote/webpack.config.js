/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */


var path = require('path');
var webpack = require('webpack');
var ExtractTextPlugin = require('extract-text-webpack-plugin');
var WebpackErrorNotificationPlugin = require('webpack-error-notification');


module.exports = {
    context: __dirname,
    entry: './main/front-end/js/main.js',
    output: {
        path: __dirname+'/main/static/main/js',
        filename: "bundle.js"
    },
    resolve: {
      root:[
        path.join(__dirname, "bower_components")
      ],
      extensions: ['', '.js','.json']
    },
    plugins: [
      /*new ExtractTextPlugin("./status/apps/main/static/main/dist/css/all.css", {
            allChunks: true
      }),*/
      new webpack.ResolverPlugin(
        new webpack.ResolverPlugin.DirectoryDescriptionFilePlugin("bower.json", ["main"])
      ),
     new webpack.ProvidePlugin({
                $: "jquery",
                jQuery: "jquery",
                'jquery-cookie': "jquery-cookie"
      }),
      new WebpackErrorNotificationPlugin(/* strategy */)
    ]
};





