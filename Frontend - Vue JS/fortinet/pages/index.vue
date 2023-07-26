<template>
  <div>
    <div class="shadow">
        <nav class="navbar navbar-light navbar-expand-md navigation-clean bg-white">
            <div class="container"><a class="navbar-brand" href="#" style="font-family: Muli, sans-serif;font-weight: bold;">Fortinet Resturant Directory</a><button class="navbar-toggler" data-toggle="collapse" data-target="#navcol-1"><span class="sr-only">Toggle navigation</span><span class="navbar-toggler-icon"></span></button>
            </div>
        </nav>
    </div>
    <div style="margin-top: 20px;">
        <div class="container">
            <div class="row">
                <div class="col-md-12">
                    <div class="card shadow">
                        <div class="card-body" style="padding-right: 50px;padding-left: 50px;padding-top: 30px;padding-bottom: 30px;">
                            <h5 class="text-center card-title">Search hundreds of restaurants around the world</h5>
                            <div class="input-group">
                                <div class="input-group-prepend"><span class="input-group-text"><i class="fa fa-search"></i></span></div><input class="form-control" type="text" placeholder="Start typing a restaurant's name..." style="font-weight: 100;font-style: normal;" v-model="search">
                                <div class="input-group-append"><button class="btn btn-danger" type="button">Search</button></div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <div>
        <div class="container">
            <div class="row d-flex">
                <div class="col-md-12">
                    <div class="card shadow" style="height: 100%;">
                        <div class="card-body">
                            <h6 class="card-title"><i class="fa fa-glass"></i>&nbsp;Select Cuisines</h6>
                            <div class="row">
                              <div class="col-md-3" v-for="(x,i) in restaurants.cui" :key="i">
                                <div class="custom-control custom-control-inline custom-checkbox"><input class="custom-control-input" :value="x" type="checkbox" :id="x" v-model="selectedcui"><label class="custom-control-label" :for="x">{{x}}</label></div>
                              </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="row d-flex">
                <div class="col-md-12">
                    <div class="card shadow">
                        <div class="card-body">
                            <h6 class="card-title"><i class="fa fa-sort-alpha-asc"></i>&nbsp;Sort by</h6>
                            <div class="row">
                                <div class="col-2">
                                    <div class="form-check"><input class="form-check-input" type="radio" id="f1" name="sort" value="f1" v-model="selectedsort"><label class="form-check-label" for="f1">Rating&nbsp;<i class="fa fa-chevron-up"></i></label></div>
                                    <div class="form-check"><input class="form-check-input" type="radio" id="f2" name="sort" value="f2" v-model="selectedsort"><label class="form-check-label" for="f2">Rating&nbsp;<i class="fa fa-chevron-down"></i></label></div>
                                </div>
                                <div class="col-2">
                                    <div class="form-check"><input class="form-check-input" type="radio" id="f3" name="sort" value="f3" v-model="selectedsort"><label class="form-check-label" for="f3">Votes&nbsp;<i class="fa fa-chevron-up"></i></label></div>
                                </div>
                                <div class="col-2">
                                    <div class="form-check"><input class="form-check-input" type="radio" id="f4" name="sort" value="f4" v-model="selectedsort"><label class="form-check-label" for="f4">Votes&nbsp;<i class="fa fa-chevron-down"></i></label></div>
                                </div>
                                <div class="col-3">
                                    <div class="form-check"><input class="form-check-input" type="radio" id="f5" name="sort" value="f5" v-model="selectedsort"><label class="form-check-label" for="f5">Avg. cost for two&nbsp;<i class="fa fa-chevron-up"></i></label></div>
                                </div>
                                <div class="col-3">
                                    <div class="form-check"><input class="form-check-input" type="radio" id="f6" name="sort" value="f6" v-model="selectedsort"><label class="form-check-label" for="f6">Avg. cost for two&nbsp;<i class="fa fa-chevron-down"></i><br></label></div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <a class="btn btn-link float-right" role="button" href="#!" @click.prevent="clear"><i class="fa fa-close"></i>&nbsp;Clear filters</a>
                </div>
            </div>
        </div>
    </div>
    <h4 class="text-center" style="margin-top: 20px;">Search Result</h4>
    <h6 class="text-center text-muted">{{result.length}} results found</h6>
    <br>
    <div>
        <div class="container">
            <div class="row d-flex">
                <div class="col-sm-12 col-md-3" v-for="(x,i) in result" :key="i">
                  <a href="#!" style="text-decoration:none" @click.prevent="showmodal(x['Restaurant Name'],x['Address'])">
                    <div class="card shadow" style="margin-bottom:10px">
                        <div class="card-body">
                            <h5 class="text-info card-title" style="font-family: Muli, sans-serif;font-weight:bold">{{x['Restaurant Name']}}<br></h5>
                            <h6 class="text-muted card-subtitle mb-2" style="font-size: 12px;" title="Average cost for two"><i class="fa fa-money"></i>&nbsp;{{x['Average Cost for two']}}&nbsp;{{x.Currency}}<br></h6>
                            <!-- <br> -->
                            <p class="text-success" style="font-size: 13px;margin-bottom:0" v-if="x['Has Table booking']=='Yes'"><i class="fa fa-check"></i>&nbsp;Table booking available</p>
                            <p class="text-danger" style="font-size: 13px;margin-bottom:0" v-else><i class="fa fa-remove"></i>&nbsp;Table booking not available</p>
                            <p class="text-success" style="font-size: 13px;" v-if="x['Has Online delivery']=='Yes'"><i class="fa fa-check"></i>&nbsp;Online delivery available</p>
                            <p class="text-danger" style="font-size: 13px;" v-else><i class="fa fa-remove"></i>&nbsp;Online delivery not available</p>
                            <div><span class="badge badge-primary" style="font-weight: 100;margin-right:5px" v-for="(y,j) in x.Cuisines" :key="j">{{y}}</span></div>
                            <br>
                            <h6 class="float-left" :style="{'color':x['Rating color']}"><i class="fa fa-star"></i>&nbsp;{{x['Aggregate rating']}} {{x['Rating text']}}</h6>
                            <h6 class="text-black-50 float-right">{{x.Votes}} votes</h6>
                        </div>
                    </div>
                  </a>
                </div>
            </div>
        </div>
        <div class="modal fade" role="dialog" tabindex="-1" id="exampleModal">
            <div class="modal-dialog modal-xl modal-dialog-centered" role="document">
                <div class="modal-content">
                    <div class="modal-header">
                        <h4 class="modal-title">{{restname}}</h4><button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button></div>
                    <div class="modal-body" style="padding: 0px;"><iframe allowfullscreen="" frameborder="0" width="100%" height="700" :src="restadd"></iframe></div>
                </div>
            </div>
        </div>
    </div>
  </div>
</template>

<script>
export default {
  data(){
    return {
      restaurants:[],
      result:[],
      selectedcui:[],
      selectedsort:'',
      search:'',
      restadd:'',
      restname:''
    }
  },
  created(){
    this.fetchall()
  },
  methods:{
    fetchall()
    {
      this.$axios.get("http://localhost:5000/getall").then(response=>{
        this.restaurants=response.data
        this.result=response.data.res
      })
    },
    showmodal(name,address){
      $(document).ready(()=>{
        this.restadd='https://www.google.com/maps/embed/v1/place?key=AIzaSyBng7HbphTIPki4LNECmUs4y0tjykem-gE&q='+address+'&zoom=14'
        this.restname=name
        $('#exampleModal').modal()
      });
    },
    clear(){
      this.search=''
      this.result=this.restaurants.res
      this.selectedcui=[]
      this.selectedsort=''
      this.restadd='',
      this.restname=''
    }
  },
  watch: {
  	'selectedsort': function(newVal, oldVal) {
    	switch (newVal) {
        case 'f1':
          this.result=this.result.sort(function(a, b) {
              var x = a['Aggregate rating']; var y = b['Aggregate rating'];
              return ((x < y) ? -1 : ((x > y) ? 1 : 0));
          });
          break;
        case 'f2':
          this.result=this.result.sort(function(a, b) {
              var x = a['Aggregate rating']; var y = b['Aggregate rating'];
              return ((x > y) ? -1 : ((x < y) ? 1 : 0));
          });
          break;
        case 'f3':
          this.result=this.result.sort(function(a, b) {
              var x = a['Votes']; var y = b['Votes'];
              return ((x < y) ? -1 : ((x > y) ? 1 : 0));
          });
          break;
        case 'f4':
          this.result=this.result.sort(function(a, b) {
              var x = a['Votes']; var y = b['Votes'];
              return ((x > y) ? -1 : ((x < y) ? 1 : 0));
          });
          break;
        case 'f5':
          this.result=this.result.sort(function(a, b) {
              var x = a['Average Cost for two']; var y = b['Average Cost for two'];
              return ((x < y) ? -1 : ((x > y) ? 1 : 0));
          });
          break;
        case 'f6':
          this.result=this.result.sort(function(a, b) {
              var x = a['Average Cost for two']; var y = b['Average Cost for two'];
              return ((x > y) ? -1 : ((x < y) ? 1 : 0));
          });
          break;

        default:
          break;
      }
    },
    'selectedcui': function(newVal, oldVal) {
      if (newVal=='')
        this.result=this.restaurants.res
      else
      	this.result = this.result.filter(f => f['Cuisines'].includes(newVal[0]));
    },
    'search': function(newVal, oldVal) {
      this.result = this.restaurants.res.filter(f => f['Restaurant Name'].toLowerCase().includes(newVal.toLowerCase()));
    }
  }

}
</script>

<style>

</style>
