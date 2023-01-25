/**
 * Sample React Native App
 * https://github.com/facebook/react-native
 *
 * @format
 */

import React, {useEffect,useState} from 'react';
import type {PropsWithChildren} from 'react';
import {
  ImageBackground,
  SafeAreaView,
  ScrollView,
  StatusBar,
  StyleSheet,
  ActivityIndicator,
  FlatList,
  Text,
  useColorScheme,
  View,
} from 'react-native';

import {
  Colors,
  DebugInstructions,
  Header,
  LearnMoreLinks,
  ReloadInstructions,
} from 'react-native/Libraries/NewAppScreen';

type SectionProps = PropsWithChildren<{
  title: string;
}>;


function Footbar({children, title}: SectionProps): JSX.Element {
  const isDarkMode = useColorScheme() === 'dark';
  return (
    <View style={styles.sectionContainer}>
      <Text
        style={[
          styles.sectionTitle,
          {
            color: isDarkMode ? Colors.white : Colors.black,
          },
        ]}>
        {title}
      </Text>
      <Text
        style={[
          styles.sectionDescription,
          {
            color: isDarkMode ? Colors.white : Colors.dark,
          },
        ]}>
        {children}
      </Text>
    </View>
  );
}

function Toolbar({children, title}: SectionProps): JSX.Element {
  const isDarkMode = useColorScheme() === 'dark';
  return (
    <View style={styles.sectionContainer}>
      <Text
        style={[
          styles.sectionTitle,
          {
            color: isDarkMode ? Colors.white : Colors.black,
          },
        ]}>
        {title}
      </Text>
      <Text
        style={[
          styles.sectionDescription,
          {
            color: isDarkMode ? Colors.white : Colors.dark,
          },
        ]}>
        {children}
      </Text>
    </View>
  );
}


function Section({children, title}: SectionProps): JSX.Element {
  const isDarkMode = useColorScheme() === 'dark';
  return (
    <View style={styles.sectionContainer}>
      <Text
        style={[
          styles.sectionTitle,
          {
            color: isDarkMode ? Colors.white : Colors.black,
          },
        ]}>
        {title}
      </Text>
      <Text
        style={[
          styles.sectionDescription,
          {
            color: isDarkMode ? Colors.light : Colors.dark,
          },
        ]}>
        {children}
      </Text>
    </View>
  );
}




type Movie = {
  id: string;
  title: string;
  releaseYear: string;
};

function TestApi():JSX.Element {
  const [isLoading, setLoading] = useState(true);
  const [data, setData] = useState<Movie[]>([]);

  const getMovies = async () => {
    try {
      const response = await fetch('https://api.nasa.gov/planetary/apod?api_key=sDNs8qATnAyQCkASC32NBbrJy7xMn4H4RnHRBm3O');
      const json = await response.json();
      setData(json);
      console.log(data);
      console.log('fui');
    } catch (error) {
      console.log('fui N');
      console.error(error);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    getMovies();
  }, []);

  return (
    <View style={styles.card}>
      {isLoading ? (
        <Text>Carregando...</Text>
      ) : (
        <Section>
        <Text style={styles.resume}><Text style={styles.highlight}> Data: </Text>{(data.date.split('-').reverse()).join('/')}</Text>
       {'\n'}
       <Text style={styles.resume}><Text style={styles.highlight}> Resumo: </Text>{data.explanation}</Text>
        </Section>

      )}
    </View>
  );
};







const image = {uri:'https://raw.githubusercontent.com/reinanbr/app_image_day/main/src/img/background.jpg'};



function App(): JSX.Element {
  const isDarkMode = useColorScheme() === 'dark';

  const backgroundStyle = {
    backgroundColor: isDarkMode ? Colors.darkest : Colors.lighter,
  };

  return (
    <SafeAreaView style={backgroundStyle}>
      <StatusBar
        barStyle={isDarkMode ? 'light-content' : 'dark-content'}
        backgroundColor={backgroundStyle.backgroundColor}
      />
      <ScrollView
        contentInsetAdjustmentBehavior="automatic"
        style={backgroundStyle}> 
      <View
          style={{flex:1,color:'red'},{
            backgroundColor: isDarkMode ? Colors.black : Colors.white,
          }}>  
          <Toolbar title="Imagem do dia - NASA"/>
    

   
                   
       <ImageBackground source={image} resizeMode="cover" style={styles.image}>
         

           
          <TestApi/> 


    </ImageBackground>


  <Footbar/>
      </View> 
      </ScrollView> 

    </SafeAreaView>
  );
}
//const { height } = Dimensions.get('window');

const styles = StyleSheet.create({
  sectionContainer: {
    marginTop: 32,
    paddingHorizontal: 24,
  },
  sectionTitle: {
    fontSize: 25,
    fontWeight: '600',
    color:'#F9E875'
  },
  red:{
    color:'#F9E875'
  },
  sectionDescription: {
    marginTop: 8,
    fontSize: 18,
    fontWeight: '400',
  },
  highlight: {
    fontWeight: '700',
  },
  resume:{
    fontSize:11,
  },
  image: {
  flex:1,
    justifyContent: 'center'}
    ,

  card:{
    flex:1,
    backgroundColor: '#000000c0',


    fontSize:30,
    color:'red',
    justifyContent: 'flex-start',
    flexDirection: 'column',
    paddingTop:0,
    paddingBottom:20,
    marginBottom:400,
    marginTop: 20,
    fontWeight:'800' // Replace by 20
  }
});

export default App;
