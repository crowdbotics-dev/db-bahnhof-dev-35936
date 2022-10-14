import { Slider } from "react-native-elements";
import { Pressable } from "react-native";
import { TextInput } from "react-native";
import React from "react";
import { View, StyleSheet } from "react-native";

const Untitled2 = ({
  navigation
}) => {
  return <View style={_styles.ehQkAXiO}>
      <View style={_styles.HyNKfUVa}></View><View style={_styles.sHBOGfVE}></View><TextInput style={_styles.NzBSeTsH}></TextInput><Pressable onPress={() => navigation.navigate("addCardDetails")} style={_styles.IBynuSqq}><View style={_styles.kWQFPvOs}></View></Pressable><Slider style={_styles.QJZScuLK} thumbStyle={{
      height: 20,
      width: 20
    }} thumbTintColor="#0000FF" maximumValue={1} minimumValue={0}></Slider></View>;
};

export default Untitled2;

const _styles = StyleSheet.create({
  ehQkAXiO: {
    backgroundColor: "#f0f0f1",
    padding: 10,
    position: "relative",
    height: "100%"
  },
  HyNKfUVa: {
    left: 11,
    top: 32,
    position: "absolute",
    height: 170,
    width: 329,
    backgroundColor: "#000000",
    borderRadius: 0,
    color: "#777777"
  },
  sHBOGfVE: {
    left: 130,
    top: 148,
    position: "absolute",
    width: 80,
    height: 80,
    backgroundColor: "#ffffff",
    borderRadius: "50%"
  },
  NzBSeTsH: {
    left: 28,
    top: 270,
    position: "absolute",
    backgroundColor: "#ffffff",
    borderColor: "#cccccc",
    width: 300,
    height: 30
  },
  kWQFPvOs: {
    left: 31,
    top: 355,
    position: "absolute",
    height: 60,
    width: 301,
    backgroundColor: "#E4E4E4",
    borderRadius: 0,
    color: "#777777"
  },
  IBynuSqq: {
    position: "unset"
  },
  QJZScuLK: {
    left: 31,
    top: 444,
    position: "absolute",
    width: 150,
    height: 40
  }
});